from ..api import AbstractBuilder, BuiltData
from ..api.actions import AbstractAction
from typing import Any, overload
import os


class TriggerBuilder(AbstractBuilder):
    def __init__(self, mod: "Mod", name: str, block_events: "BlockEventsBuilder"):
        super().__init__(mod)
        self._name = name
        self._block_events = block_events
        self._data = []

    @overload
    def with_action(self, action_id: str, parameters: dict) -> "TriggerBuilder":
        ...

    @overload
    def with_action(self, action: dict) -> "TriggerBuilder":
        ...

    @overload
    def with_action(self, action: list[dict]) -> "TriggerBuilder":
        ...

    def with_action(self, action, parameters = None) -> "TriggerBuilder":
        if isinstance(action, dict):
            self._data.append(action)
        if isinstance(action, list):
            [self.with_action(item) for item in action]
        elif isinstance(action, AbstractAction):
            self._data.append({"actionId": action.id, "parameters": action.data})
        elif isinstance(action, str):
            self.with_action({
                "actionId": action,
                "parameters": parameters
            })
        else:
            raise RuntimeError("Cannot add action of type:", type(action))
        return self

    def build(self) -> "BlockEventsBuilder":
        self._block_events._data["triggers"][self._name] = self._data
        return self._block_events


class BlockEventsBuilder(AbstractBuilder):
    def __init__(self, mod: "Mod", name: str):
        super().__init__(mod)
        self._name = name
        self._data = {
            "parent": "base:block_events_default",
            "stringId": f"{mod.namespace}:{name}",
            "triggers": {}
        }

    def with_parent(self, parent_id: str) -> "BlockEventsBuilder":
        self._data["parent"] = parent_id
        return self

    def with_trigger(self, id: str) -> "TriggerBuilder":
        return TriggerBuilder(self._mod, id, self)

    on = with_trigger

    def on_break(self)    -> "TriggerBuilder": return self.with_trigger("onBreak")
    def on_place(self)    -> "TriggerBuilder": return self.with_trigger("onPlace")
    def on_interact(self) -> "TriggerBuilder": return self.with_trigger("onInteract")
    def on_explode(self)  -> "TriggerBuilder": return self.with_trigger("onExplode")

    def build(self) -> BuiltData:
        path = os.path.join("block_events", f"{self._name}.json")
        return BuiltData(path, self._data)
