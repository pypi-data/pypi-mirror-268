# Cosmic DatAPI

Basically a library to create data mods in Cosmic Reach really fast.

**Example:**
```python3
from cosmic_datapi import Mod

MOD = Mod("example_mod")

(MOD.block("example_block")
    .with_state("default")
        .with_model("model_cheese")
        .with_light(14, 13, 12)
        .build()
    .build())

MOD.build()
```
