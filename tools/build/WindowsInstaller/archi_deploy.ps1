cd C:\archi-ve\FreeCAD
git pull
cd C:\archi-ve\FreeCAD\src\mod
git pull
cd C:\archi-ve\FreeCAD\tools\build\WindowsInstaller\deploy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
.\pipeline.ps1