# ========================
# CONFIGURATION VARIABLES
# ========================

param (
    [Parameter(Mandatory = $true)]
    [string]$SRC_DIR,

    [Parameter(Mandatory = $true)]
    [string]$BUILD_DIR,

    [Parameter(Mandatory = $true)]
    [string]$LIBPACK_DIRECTORY,

    [Parameter(Mandatory = $true)]
    [string]$TOOLS_DIRECTORY,

    [Parameter(Mandatory = $true)]
    [string]$VS2022_DIRECTORY

)

if (-Not (Test-Path $SRC_DIR)) {
    Write-Host " FreeCAD not found at: $SRC_DIR" -ForegroundColor Red
    exit 1
}

if (-Not (Test-Path $BUILD_DIR)) {
    Write-Host " Build dir not found at: $BUILD_DIR. Making new one.." -ForegroundColor Yellow
    New-Item -Path $BUILD_DIR -ItemType Directory -Force
}

if (-Not (Test-Path $LIBPACK_DIRECTORY)) {
    Write-Host " LibPack not found at: $LIBPACK_DIRECTORY" -ForegroundColor Red
    exit 1
}

if (-Not (Test-Path $TOOLS_DIRECTORY)) {
    Write-Host " Tools not found at: $TOOLS_DIRECTORY" -ForegroundColor Red
    exit 1
}

if (-Not (Test-Path $VS2022_DIRECTORY)) {
    Write-Host " Visual Studio 2022 not found at: $VS2022_DIRECTORY" -ForegroundColor Red
    exit 1
}

# ========================
# RUN CMAKE
# ========================
$flags = Get-Content $SRC_DIR"\tools\build\freecad_flags.txt"
# Pattern to match LibPack path (escaped for regex)
$libpackPattern = "C:/archi-ve/LibPack-[^/]+(/.+)"
$toolsPattern = "C:/archi-ve/tools[^/]+(/.+)"
$msvcPattern = "C:/Program Files/Microsoft Visual Studio/2022/Community[^/]+(/.+)"
# Replace paths
$updatedFlags = $flags | ForEach-Object {
    if ($_ -match $libpackPattern) {
        $subpath = $Matches[1] -replace "/", "\"
        $_ -replace $libpackPattern, "$LIBPACK_DIRECTORY$subpath"
    } 
    elseif ($_ -match $toolsPattern) {
        $subpath = $Matches[1] -replace "/", "\"
        $_ -replace $toolsPattern, "$TOOLS_DIRECTORY$subpath"
    } 
    elseif ($_ -match $msvcPattern) {
        $subpath = $Matches[1] -replace "/", "\"
        $_ -replace $msvcPattern, "$VS2022_DIRECTORY$subpath"
    } 
    else {
        $_
    }
}
Push-Location $SRC_DIR

cmake -S $SRC_DIR -B $BUILD_DIR $updatedFlags
  
Pop-Location
# Optional: build
# cmake --build $BUILD_DIR --config Release --parallel
