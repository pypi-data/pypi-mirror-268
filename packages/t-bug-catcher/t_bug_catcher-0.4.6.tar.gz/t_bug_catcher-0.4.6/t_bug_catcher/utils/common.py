import copy
import traceback
from datetime import date, datetime
from json import JSONEncoder
from pathlib import Path
from types import TracebackType
from typing import List

from ..config import CONFIG


class Encoder(JSONEncoder):
    """This class is used to encode the Episode object to json."""

    def default(self, o):
        """This method is used to encode the Episode object to json.

        Args:
            o (object): The object to be encoded.

        Returns:
            str: The json string.
        """
        object_copy = copy.deepcopy(o)
        try:
            if hasattr(object_copy, "__dict__"):
                keys_to_remove = [
                    key
                    for key in object_copy.__dict__.keys()
                    if any(s in str(key).lower() for s in CONFIG.KEYS_TO_REMOVE)
                ]
                for key in keys_to_remove:
                    del object_copy.__dict__[key]
                return {str(key): str(value) for key, value in object_copy.__dict__.items()}
            if isinstance(object_copy, (datetime, date)):
                return object_copy.isoformat()
            if isinstance(object_copy, Path):
                return str(object_copy)
            return super().default(self, object_copy)
        except TypeError:
            return str(object_copy)


def get_frames(exc_traceback: TracebackType) -> List:
    """Get the frames of the exception.

    Args:
        exc_traceback (TracebackType): The traceback of the exception.

    Returns:
        List: The frames of the exception.
    """
    return [
        frame for frame in traceback.extract_tb(exc_traceback) if "site-packages" not in str(frame.filename).lower()
    ]


def convert_keys_to_primitives(data: dict) -> dict:
    """A function that recursively converts keys in a nested dictionary to primitives.

    Args:
        data (dict): The input dictionary to convert keys.

    Returns:
        dict: A new dictionary with keys converted to strings.
    """
    new_dict = {}
    for key, value in data.items():
        if isinstance(value, dict):
            new_dict[str(key)] = convert_keys_to_primitives(value)
        else:
            new_dict[str(key)] = value
    return new_dict
