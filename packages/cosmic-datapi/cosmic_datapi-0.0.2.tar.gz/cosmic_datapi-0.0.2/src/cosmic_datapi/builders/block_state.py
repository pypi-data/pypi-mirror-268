from ..api import AbstractBuilder, BuiltData
from typing import Any


class BlockStateBuilder(AbstractBuilder):
    def __init__(self, mod: "Mod", name: str, block: "BlockBuilder"):
        super().__init__(mod)
        self._name = name
        self._block = block
        self._data = {
        #   "parameter":            None, # default value
            "modelName":            None,
            "isOpaque":             None, # true
            "isTransparent":        None, # true
            "generateSlabs":        None, # false
            "catalogHidden":        None, # false
            "lightAttenuation":     None, # 0
            "canRaycastForBreak":   None, # true
            "canRaycastForPlaceOn": None, # true
            "canRaycastForReplace": None, # true
            "walkThrough":          None, # false
            "lightLevelRed":        None, # 0
            "lightLevelGreen":      None, # 0
            "lightLevelBlue":       None, # 0
        }

    def set(self, option: str, value: Any) -> "BlockStateBuilder":
        self._data[option] = value
        return self

    def with_model(self, id: str) -> "BlockStateBuilder":
        return self.set("modelName", id)

    def with_slabs(self) -> "BlockStateBuilder":
        return self.set("generateSlabs", True)

    def with_light(self, r: int, g: int, b: int) -> "BlockStateBuilder":
        self.set("lightLevelRed", r)
        self.set("lightLevelGreen", g)
        self.set("lightLevelBlue", b)
        return self

    def with_block_events(self, id: str) -> "BlockStateBuilder":
        return self.set("blockEventsId", id)

    def with_no_catalog_entry(self) -> "BlockStateBuilder":
        return self.set("catalogHidden", True)

    def with_no_collision(self) -> "BlockStateBuilder":
        return self.set("walkThrough", True)

    def build(self) -> "BlockBuilder":
        data = {key: val for key, val in self._data.items() if val is not None}
        if "modelName" not in data:
            print(f"error: block state {self._mod.namespace}:{self._block._name}[{self._name}] has no model.")
        self._block._data["blockStates"][self._name] = data
        return self._block
