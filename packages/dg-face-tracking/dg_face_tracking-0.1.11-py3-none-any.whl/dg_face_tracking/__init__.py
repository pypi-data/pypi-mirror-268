from pathlib import Path
Path(__file__).resolve()

from ._version import __version__, __version_info__

from .track_faces import track_faces
from .Face2ID.face2id import face2id, face2id_stop, face2id_reset


def _command_entrypoint(arg_str=None):
    track_faces()

