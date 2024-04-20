from . import builders
from typing import Union
import tqdm
import os
import shutil


class Mod:
    def __init__(self, namespace: str):
        self.namespace = namespace
        self.output_dir = os.path.join("build", self.namespace)
        self._generators = []
        self._included_paths = []

    def build(self):
        total = len(self._generators) + len(self._included_paths)
        with tqdm.tqdm(desc = f"Building {self.namespace}", total = total) as bar:
            for generator in self._generators:
                generator.build().save(self.output_dir)
                bar.update()

            bar.set_description("Including content...")
            for path in self._included_paths:
                if os.path.isfile(path):
                    shutil.copyfile(path, self.output_dir)
                else:
                    shutil.copytree(path, self.output_dir, dirs_exist_ok = True)
                bar.update()

            bar.set_description("Done!")
            bar.close()

    def _generator(self, clazz, *args, **kwargs):
        builder = clazz(self, *args, **kwargs)
        self._generators.append(builder)
        return builder

    def block(self, name: str) -> builders.BlockBuilder:
        return self._generator(builders.BlockBuilder, name)

    def block_events(self, name: str) -> builders.BlockEventsBuilder:
        return self._generator(builders.BlockEventsBuilder, name)

    def model(self, name: str) -> builders.ModelBuilder:
        return self._generator(builders.ModelBuilder, name)

    def include(self, path: Union[str, list[str]]) -> "Mod":
        if not (os.path.exists(path) or os.path.isfile(path)):
            print(f"error: {path} is included but does not exist.")
            exit(1)

        if type(path) == list:
            self._included_paths.extend(path)
        else:
            self._included_paths.append(path)

        return self
