#!/usr/bin/env sh
# Installs a mod in `build`
mkdir -p ~/.local/share/cosmic-reach/mods/assets/
cp -r ./build/$1/* ~/.local/share/cosmic-reach/mods/assets/
