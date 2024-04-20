from ..api import AbstractBuilder, BuiltData
from .block_state import BlockStateBuilder
import os


class ModelBuilder(AbstractBuilder):
    def __init__(self, mod: "Mod", name: str):
        super().__init__(mod)
        self._name = name
        self._data = {
            "parent": "cube",
            "textures": {}
        }

    def with_parent(self, id: str) -> "ModelBuilder":
        self._data["parent"] = id
        return self

    def with_texture(self, kind: str, file_name: str) -> "ModelBuilder":
        self._data["textures"]["kind"] = {
            "fileName": file_name
        }
        return self

    def build(self) -> BuiltData:
        path = os.path.join("blocks", f"{self._name}.json")
        return BuiltData(path, self._data)
