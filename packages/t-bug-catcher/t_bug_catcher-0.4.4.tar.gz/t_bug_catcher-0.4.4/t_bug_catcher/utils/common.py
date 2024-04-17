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
        try:
            if hasattr(o, "__dict__"):
                keys_to_remove = [
                    key for key in o.__dict__.keys() if any(s in str(key).lower() for s in CONFIG.KEYS_TO_REMOVE)
                ]
                for key in keys_to_remove:
                    del o.__dict__[key]
                return {str(key): str(value) for key, value in o.__dict__.items()}
            if isinstance(o, (datetime, date)):
                return o.isoformat()
            if isinstance(o, Path):
                return str(o)
            return super().default(self, o)
        except TypeError:
            return str(o)


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
