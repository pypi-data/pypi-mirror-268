import degirum as dg
import numpy as np

from typing import Union

from pathlib import Path
Path(__file__).resolve()

from .face2id_proc import Face2ID_Proc, unknown, error


# Global Face to ID processing instance
gl_proc: Union[Face2ID_Proc, None] = None


def result2json(result: str):
    label, err_msg = (result, "") if error not in result else ("", result)
    return f"""{{"label": "{label}", "error": "{err_msg}" }}"""


def face2id(img: Union[str, np.ndarray],
            deployment: str = "docker",
            async_support: bool = False,
            verbose: bool = False) -> str:
    """
    Face image to Person ID
    img : str or ndarray: face image as base64 encoded png or numpy array
    deployment: ["cloud", "local", "docker"]
    async_support: bool: do we need to enable async support
    verbose: bool: for testing purpose only
    return: json '{"label": "<some label or empty string>", "error": "<error message or empty string>"}'.
    """
    global gl_proc

    if img is None:
        return result2json(f"{error}: nNone image is passed to face2id processor")

    if gl_proc is None:
        # instantiate processor
        try:
            gl_proc = Face2ID_Proc(deployment=deployment, async_support=async_support, verbose=verbose)
        except Exception as e:
            return result2json(f"{error}: unable to create face2id processor: {str(e)}")

    try:
        # identify the face image
        label = gl_proc.face2id(img)
        return result2json(label)
    except Exception as e:
        gl_proc.stop()
        gl_proc = None
        return result2json(f"{error}: unresolved exception {str(e)}")



