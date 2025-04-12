# This is a windows deploy tutorial

## Setup necessary files
You need to install 
    https://github.com/touch-topnotch/FreeCAD

git clone --recurse-submodules https://github.com/touch-topnotch/FreeCAD.git

```cd /path/to/freecad/src/mod/```
git clone https://github.com/touch-topnotch/archi


    https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/3.1.0
    https://drive.google.com/file/d/1JrmjbXEY5NawL__FSzQZGvsckgrl8J9g/view?usp=sharing
    https://visualstudio.microsoft.com/ru/

## Prepare for deploy
1. turn on VisualStudioInstaller

select "Edit/Изменить -> Development of Classic C++ Applications -> set flag MSVC of version 143"

-> "Edit/Изменть"


2. in powershell - ```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```
3. go to /path/to/freecad/tools/build/WindowsInstaller/deploy
4. open ```pipeline.ps1```
## IT IS VERY IMPORTANT TO SET CORRECT DIRECTORIES, DOUBLE CHECK IT
5. edit path variables:
```
    $SRC_DIR = "C:\archi-ve\FreeCAD"
    $BUILD_DIR = "C:\archi-ve\FreeCAD\build"
    $TOOLS_DIR = "C:\archi-ve\tools"
    $LIBPACK_DIRECTORY = "C:\archi-ve\LibPack-1.1.0-v3.1.0-Release"
    $VS2022_DIRECTORY = "C:\Program Files\Microsoft Visual Studio\2022\Community"
```
# Deploy
run powershell as administrator
1. ```cd path/to/freecad/tools/build/WindowsInstaller/deploy```
2. ```./pipeline.ps1```

Done!