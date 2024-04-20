from ..api import AbstractBuilder, BuiltData
from .block_state import BlockStateBuilder
import os


class BlockBuilder(AbstractBuilder):
    def __init__(self, mod: "Mod", name: str):
        super().__init__(mod)
        self._name = name
        self._data = {
            "stringId": f"{mod.namespace}:{name}",
            "defaultParams": {},
            "blockStates": {}
        }

    def with_state(self, state_name: str) -> BlockStateBuilder:
        return BlockStateBuilder(self._mod, state_name, self)

    def with_default_params(self, params: dict) -> "BlockBuilder":
        self._data["defaultParams"] = params
        return self

    def build(self) -> BuiltData:
        path = os.path.join("blocks", f"{self._name}.json")
        return BuiltData(path, self._data)
