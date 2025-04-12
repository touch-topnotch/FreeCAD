
param (
    [Parameter(Mandatory = $true)]
    [string]$buildDir,

    [Parameter(Mandatory = $true)]
    [string]$vs2022
)


# Ensure Admin rights
$IsAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $IsAdmin) {
    Write-Host " This script must be run as Administrator." -ForegroundColor Red
    exit 1
}

# Define paths
$vsDevCmd = Join-Path $vs2022 "\Common7\Tools\VsDevCmd.bat"
$tempBat = "$env:TEMP\freecad_build.bat"

# Check VS path
if (-Not (Test-Path $vsDevCmd)) {
    Write-Host " Could not find VsDevCmd.bat at: $vsDevCmd" -ForegroundColor Red
    exit 1
}

# Write temp .bat file
@"
@echo off
call "$vsDevCmd"
cd /d "$buildDir"
echo Building FreeCAD INSTALL project...
msbuild INSTALL.vcxproj /p:Configuration=Release
"@ | Set-Content -Encoding ASCII $tempBat
$logFile = Join-Path $buildDir "install_build.log"
# Run the .bat file in cmd.exe
cmd.exe /c "`"$tempBat`"" > "`"$logFile`"" 2>&1

# Check if the batch file failed
if ($LASTEXITCODE -ne 0) {
    Write-Host " Batch script failed with exit code $LASTEXITCODE"
    Remove-Item $tempBat -Force
    exit 1
}

# Optional: Remove the temp .bat after successful execution
Remove-Item $tempBat -Force
Write-Host "Batch script completed successfully."
