@echo off
call conda activate freecad
mamba run -n freecad cmake %*

