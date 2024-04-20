from typing import NamedTuple
from abc import ABC
import os
import json


class BuiltData(NamedTuple):
    """A holder class containing the file path for existing data in a mod.
    """
    file_path: str
    json_data: dict

    def save(self, path: str):
        path = os.path.join(path, self.file_path)
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok = True)
        with open(path, "w+") as fp:
            json.dump(self.json_data, fp, indent=4)


class AbstractBuilder(ABC):
    def __init__(self, mod: "Mod"):
        self._mod = mod

    def build(self) -> BuiltData:
        pass
