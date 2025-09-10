
set "PIXI_PATH=C:\Program Files\pixi"
set "PATH=%PIXI_PATH%;%PATH%"

echo Initializing VS and Conda...
call "C:/Program Files/Microsoft Visual Studio/2022/Community/Common7/Tools/VsDevCmd.bat" -arch=x64 -host_arch=x64
call "C:/Users/Administrator/miniconda3/Scripts/activate.bat" base
echo Testing conda command:
conda --version
echo Testing pixi command:
pixi --version