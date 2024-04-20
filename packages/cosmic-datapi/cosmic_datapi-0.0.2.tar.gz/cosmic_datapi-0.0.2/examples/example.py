from cosmic_datapi import Mod
from cosmic_datapi.api.actions import ActionReplaceBlockState


MODID = "example"
MOD = Mod(MODID)


(MOD.block_events("block_events_example")
    .on_interact()
        .with_action(ActionReplaceBlockState(f"base:air[default]"))
        .with_action(ActionReplaceBlockState(f"{MODID}:block_example[default]", y_off = 1))
        .build()
    .build())

(MOD.block("block_example")
    .with_state("default")
        .with_block_events("block_events_example")
        .with_model("model_cheese")
        .build()
    .build())


MOD.build()
