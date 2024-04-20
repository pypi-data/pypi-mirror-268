from ..builders import ModelBuilder

_simple_model = lambda kind: lambda mod, name, texture: ModelBuilder(mod, name).with_texture(kind, texture)
model_top = _simple_model("top")
model_slab_top = _simple_model("slab_top")
model_bottom = _simple_model("bottom")
model_slab_bottom = _simple_model("slab_bottom")
model_side = _simple_model("side")
model_slab_side = _simple_model("slab_side")
model_all = _simple_model("all")
