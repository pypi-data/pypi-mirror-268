from typing import Optional, Any
from abc import ABC


class AbstractAction(ABC):
    def __init__(self, id: str):
        self.id = id
        self.data = {}

    def set(self, param: str, value: Any) -> "AbstractAction":
        self.data[param] = value
        return self

    def with_tick_delay(self, delay: int) -> "AbstractAction":
        return self.set("tickDelay", delay)


class AbstractOffsetAction(AbstractAction):
    def __init__(self, id: str, x_off: int = 0, y_off: int = 0, z_off: int = 0):
        super().__init__(id)
        self.data["xOff"] = x_off
        self.data["yOff"] = y_off
        self.data["zOff"] = z_off


class ActionReplaceBlockState(AbstractOffsetAction):
    def __init__(self, state: str, x_off: int = 0, y_off: int = 0, z_off: int = 0):
        super().__init__("base:replace_block_state", x_off, y_off, z_off)
        self.data["blockStateId"] = state


class ActionExplode(AbstractOffsetAction):
    def __init__(self, radius: int = 5, state: Optional[str] = None, x_off: int = 0, y_off: int = 0, z_off: int = 0):
        super().__init__("base:explode", x_off, y_off, z_off)
        self.data["radius"] = radius
        self.data["blockStateId"] = state if state is not None else "base:air[default]"


class ActionPlaySound2D(AbstractAction):
    def __init__(self, sound: str, volume: int = 1, pitch: int = 1, pan: int = 0):
        super().__init__("base:play_sound_2d")
        self.data["sound"] = sound
        self.data["volume"] = volume
        self.data["pitch"] = pitch
        self.data["pan"] = pan


class ActionSetBlockStateParams(AbstractOffsetAction):
    def __init__(self, params: dict, x_off: int = 0, y_off: int = 0, z_off: int = 0):
        super().__init__("base:set_block_state_params", x_off, y_off, z_off)
        self.data["params"] = params


class ActionRunTrigger(AbstractOffsetAction):
    def __init__(self, trigger_id: str, x_off: int = 0, y_off: int = 0, z_off: int = 0):
        super().__init__("base:run_trigger", x_off, y_off, z_off)
        self.data["triggerId"] = trigger_id


class ActionSetCuboid(AbstractAction):
    def __init__(
        self,
        x1_off: int,
        y1_off: int,
        z1_off: int,
        x2_off: int,
        y2_off: int,
        z2_off: int,
        block_state_id: Optional[str] = None,
        trigger_before_set_id: Optional[str] = None,
        trigger_after_set_id: Optional[str] = None
    ):
        super().__init__("base:set_cuboid")
        self.data["x1Off"] = x1_off
        self.data["y1Off"] = y1_off
        self.data["z1Off"] = z1_off
        self.data["x2Off"] = x2_off
        self.data["y2Off"] = y2_off
        self.data["z2Off"] = z2_off
        if block_state_id is not None:
            self.data["blockStateId"] = block_state_id
        if trigger_before_set_id is not None:
            self.data["triggerBeforeSetId"] = trigger_before_set_id
        if trigger_after_set_id is not None:
            self.data["triggerAfterSetId"] = trigger_after_set_id


class ActionSetSphere(AbstractOffsetAction):
    def __init__(
        self,
        radius: int,
        block_state_id: Optional[str] = None,
        x_off: int = 0,
        y_off: int = 0,
        z_off: int = 0,
        trigger_before_set_id: Optional[str] = None,
        trigger_after_set_id: Optional[str] = None
    ):
        super().__init__("base:set_sphere", x_off, y_off, z_off)
        self.data["radius"] = radius
        if block_state_id is not None:
            self.data["blockStateId"] = block_state_id
        if trigger_before_set_id is not None:
            self.data["triggerBeforeSetId"] = trigger_before_set_id
        if trigger_after_set_id is not None:
            self.data["triggerAfterSetId"] = trigger_after_set_id


class ActionSetSphericalSegment(AbstractOffsetAction):
    def __init__(
        self,
        radius: int,
        angle_deg: int,
        block_state_id: Optional[str] = None,
        x_off: int = 0,
        y_off: int = 0,
        z_off: int = 0,
        x_normal: int = 0,
        y_normal: int = 0,
        z_normal: int = 0,
        trigger_before_set_id: Optional[str] = None,
        trigger_after_set_id: Optional[str] = None
    ):
        super().__init__(x_off, y_off, z_off)
        self.data["radius"] = radius
        self.data["angleDeg"] = angle_deg
        self.data["xNormal"] = x_normal
        self.data["yNormal"] = y_normal
        self.data["zNormal"] = z_normal
        if block_state_id is not None:
            self.data["blockStateId"] = block_state_id
        if trigger_before_set_id is not None:
            self.data["triggerBeforeSetId"] = trigger_before_set_id
        if trigger_after_set_id is not None:
            self.data["triggerAfterSetId"] = trigger_after_set_id


"""Adds the default onBreak actions to a given TriggerBuilder
"""
default_on_break_actions = [
    {
        "actionId": "base:replace_block_state",
        "parameters": {
            "xOff": 0,
            "yOff": 0,
            "zOff": 0,
            "blockStateId": "base:air[default]"
        }
    },
    {
        "actionId": "base:play_sound_2d",
        "parameters": {
            "sound": "block-break.ogg",
            "volume": 1,
            "pitch": 1,
            "pan": 0
        }
    }
]

"""Adds the default onPlace actions to a given TriggerBuilder
"""
default_on_place_actions = [
    {
        "actionId": "base:replace_block_state",
        "parameters": {
            "xOff": 0,
            "yOff": 0,
            "zOff": 0,
            "blockStateId": "self"
        }
    },
    {
        "actionId": "base:play_sound_2d",
        "parameters": {
            "sound": "block-place.ogg",
            "volume": 1,
            "pitch": 1,
            "pan": 0
        }
    }
]
