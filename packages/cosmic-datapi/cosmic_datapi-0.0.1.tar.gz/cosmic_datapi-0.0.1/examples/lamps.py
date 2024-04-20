# This script will generate a lamp for every single possible color in CR.

from cosmic_datapi import Mod
from cosmic_datapi.api.actions import ActionReplaceBlockState


MODID = "lamps"
MOD = Mod(MODID)


def make_light(r: int, g: int, b: int):
    block_id = f"{MODID}_block_light_{r}_{g}_{b}"
    events_id = f"{MODID}_block_events_light_{r}_{g}_{b}"

    (MOD.block_events(events_id + "_off")
        .on_interact()
            .with_action(ActionReplaceBlockState(MODID + ":" + block_id + "[on]"))
        .build())

    (MOD.block_events(events_id + "_on")
        .on_interact()
            .with_action(ActionReplaceBlockState(MODID + ":" + block_id + "[off]"))
        .build())

    (MOD.block(block_id)
        .with_state("off")
            .with_model("model_light_off")
            .with_block_events(f"{MODID}:{events_id}_off")
            .build()
        .with_state("on")
            .with_model("model_light_azure")
            .with_block_events(f"{MODID}:{events_id}_on")
            .with_light(r, g, b)
            .build()
        .build())


for r in range(0, 16):
    for g in range(0, 16):
        for b in range(0, 16):
            make_light(r, g, b)


MOD.build()
