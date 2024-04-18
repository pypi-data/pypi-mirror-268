import os
from typing import Union

from threading import Thread, Event, Lock
from queue import Queue, Full, Empty

import numpy as np
import base64
import time
from validators import ipv4, url
from names_generator import generate_name

import cv2

import degirum as dg
import degirum_tools

from pathlib import Path
Path(__file__).resolve()

from ..Database.vectstore import VectStore

default_config = {
    'sure_th': 0.1,
    'accept_th': 0.35,
    'reject_th': 0.60,

    'path2db': "./vectdb.pkl",

    'model': {
        'cloud_url': "https://cs.degirum.com/degirum/Barkas",
        'model': "facenet--160x160_float_trt_gpu_1",
        'input_image_format': "RAW",
        'input_numpy_colorspace': "RGB",
        'input_letterbox_fill_color': [114, 114, 114]
    }
}

q_maxsize = 16
max_timeout = 1.0

unknown = "unknown"
error = "face2id error"


class Face2ID_Proc:
    """
    Face2ID_Proc: implements Face to Label functionality
    """
    def __init__(self, deployment="docker", async_support=False, verbose=False):
        """
        deployment: ["cloud", "local", "docker"]
        async_support: bool: do we need to enable async support
        verbose: bool: for testing purpose only
        """
        self.deployment = deployment

        self.q_in = Queue(maxsize=q_maxsize)
        self.q_res = Queue(maxsize=q_maxsize)
        self.q_out_dict = {}

        self.stop_event = Event()
        self.lock = Lock()
        self.proc_thread = None
        self.result_thread = None

        self.sure_th   = 0.1
        self.accept_th = 0.35
        self.reject_th = 0.55

        generate_name(seed=42)

        self.embeds_model = None

        self.path2db = ""
        self.vstore = VectStore(max_size=32)

        self.debug = verbose
        self.apply_config()

        if async_support:
            # enables async processing
            self.start()

    def face2id(self, img:  Union[str, np.ndarray]) -> str:
        """
        Find id of a given face image. Synchronous version
        img : str or ndarray: face image as base64 encoded png or numpy array
        return: person id or 'unknown' or error message
        """
        self.lock.acquire()
        try:
            img = self.decode(img)
            embeds = self.get_embeds(img)
            class_id, label, dist = self.get_label(embeds)
            self.update_db(class_id, label, embeds, dist)
            return label
        except Exception as e:
            return f"{error}: {str(e)}"
        finally:
            self.lock.release()

    def face2id_async(self, img: Union[str, np.ndarray], client_id=0):
        """
        Find id of a given face image. Asynchronous version. Make sure that self was created with async_support=True.
        img : str or ndarray: face image as base64 encoded png or numpy array
        return: person id or 'unknown' or error message
        """
        if not self.is_running():
            return f"{error}: async support is not enabled"

        try:
            self.q_in.put((img, client_id), timeout=max_timeout)
        except Full:
            return f"{error}: input queue is full"
        except:
            return f"{error}: unknown exception"

        try:
            return self.q_out_dict[client_id].get(timeout=max_timeout)
        except Empty:
            return f"{error}: output queue is empty"
        except:
            return f"{error}: unknown exception"

    def apply_config(self):
        cfg = default_config

        self.sure_th   = cfg.setdefault('sure_th', 0.1)
        self.accept_th = cfg.setdefault('accept_th', 0.35)
        self.reject_th = cfg.setdefault('reject_th', 0.55)

        self.init_embedder(default_config['model'])

        self.path2db = cfg.setdefault('path2db', "")
        if self.path2db != "":
            try:
                self.vstore.load(self.path2db)
            except:
                # unable to load db, continue with the empty one
                pass

    def init_embedder(self, cfg):
        cfg = default_config['model']

        cloud_url = cfg.setdefault('cloud_url', "")
        model_name = cfg['model']
        local_zoo_path = cfg.setdefault('local_zoo_path', "")

        if "cloud" in self.deployment:
            zoo = dg.connect(dg.CLOUD, cloud_url, degirum_tools.get_token())
        elif "local" in self.deployment:
            model_path = os.path.join(local_zoo_path, model_name, model_name + '.json')
            zoo = dg.connect(dg.LOCAL, model_path)
        elif ipv4(self.deployment):
            zoo = dg.connect(self.deployment)
        elif "docker" in self.deployment:
            zoo = dg.connect("127.0.0.1")
        else:
            raise Exception(f"{error}: config: unknown deployment: {self.deployment}")

        model = zoo.load_model(model_name)
        model.input_image_format = cfg['input_image_format']
        input_letterbox_fill_color = cfg.setdefault('input_letterbox_fill_color', [114, 114, 114])
        model.input_letterbox_fill_color = tuple(input_letterbox_fill_color)
        model.input_numpy_colorspace = cfg.setdefault('input_numpy_colorspace', "BGR")
        model.input_pad_method = cfg.setdefault('input_pad_method', "letterbox")
        self.embeds_model = model

    def start(self):
        self.proc_thread = Thread(target=self.proc_input)
        self.proc_thread.start()
        self.proc_thread = Thread(target=self.proc_result)
        self.proc_thread.start()
        while not self.is_running():
            time.sleep(0.01)

    def is_running(self):
        return (self.proc_thread is not None and self.result_thread is not None and
                self.proc_thread.is_alive()  and self.result_thread.is_alive())

    def stop(self):
        self.stop_event.set()
        if self.proc_thread is not None and self.proc_thread.is_alive():
            self.proc_thread.join()
        if self.result_thread is not None and self.result_thread.is_alive():
            self.result_thread.join()

    def result_out(self, client_id, label):
        q_out = self.q_out_dict.setdefault(client_id, Queue(maxsize=q_maxsize))
        try:
            return q_out.put(label, timeout=max_timeout)
        except Full:
            return f"{error}: output queue for {client_id} is full"
        except:
            return f"{error}: unknown exception"

    def data_source(self):
        while not self.stop_event.is_set():
            try:
                img, client_id = self.q_in.get(timeout=0.1)
                if img is None:
                    break
                yield img, client_id
            except Empty:
                continue

    def proc_input(self):
        while not self.stop_event.is_set():
            try:
                for res in self.embeds_model.predict_batch(self.data_source()):
                    self.q_res.put(res)
                self.q_res.put_nowait(None)
                break
            except Exception as e:
                print("FaceEmbedder: run: " + str(e))
        # Stop result_process thread
        self.q_res.put(None)
        self.result_thread.join()

    def proc_results(self):
        while not self.stop_event.is_set():
            try:
                result = self.q_res.get(timeout=0.1)
                if result is None:
                    break
            except Empty:
                continue

            if len(result.results) == 0 or 'data' not in result.results[0]:
                continue

            embeds = result.results[0]['data'].flatten()
            client_id = result.info
            try:
                class_id, label, dist = self.get_label(embeds)
                self.update_db(class_id, label, embeds, dist)
                self.result_out(client_id, label)
            except Exception as e:
                self.result_out(client_id, f"{error}: {str(e)}")

    def decode(self, img):
        if isinstance(img, np.ndarray):
            pass
        elif isinstance(img, bytes):
            np_arr = np.frombuffer(img, np.uint8)
            if np_arr is None or np_arr.size == 0:
                raise Exception(f"{error}: unable to decode bytes")
            img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            if img is None:
                raise Exception(f"{error}: unable to decode image from bytes")
        elif isinstance(img, str):
            np_arr = np.frombuffer(base64.b64decode(img), np.uint8)
            if np_arr is None or np_arr.size == 0:
                raise Exception(f"{error}: unable to decode base64")
            img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            if img is None:
                raise Exception(f"{error}: unable to decode image")
        else:
            raise Exception(f"{error}: image in unknown format")

        if self.debug:
            cv2.imshow("test", img)
            cv2.waitKey(1)

        return img

    def get_embeds(self, img):
        result = self.embeds_model(img)
        if len(result.results) == 0 or 'data' not in result.results[0]:
            raise Exception("get_embeds: ")

        embeds = result.results[0]['data'].flatten()
        norm = np.linalg.norm(embeds)
        embeds /= norm
        return embeds

    def get_label(self, embeds):
        embeds = np.array(embeds)
        # search in saved face embeddings db
        results = self.vstore.search(embeds, 5, 1)
        dist = 999.9
        if len(results) > 0:
            dist, class_id, label, _ = results[0]
            # print(f"update_object_id search: score: {score:.3f}; object_id: {object_id}; label: {label}")
            if dist < self.accept_th:
                return class_id, label, dist
        return -1, unknown, dist

    def update_db(self, class_id, label, embeds, dist):
        if unknown not in label.lower():
        # known person
            if dist > self.sure_th:
                # distance is not too small => worth to add this face of a known person
                self.vstore.add(class_id, embeds, label)
        else:
        # unknown person
            if class_id != -1:
                # it is a "unsure" person => just add it
                label = self.vstore.get_class_label(class_id)
                if label is None:
                    raise Exception(f"update_db: no label corresponding to class_id {class_id}")
                self.vstore.add(class_id, embeds, label)
            else:
                if dist > self.reject_th:
                    # dist is big enough => we are sure that's a new person
                    self.vstore.dump(self.path2db)
                    class_id = self.vstore.num_classes()
                    label = generate_name(style='capital')
                    self.vstore.add(class_id, embeds, label)








