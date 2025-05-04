# ========================
# CONFIGURATION VARIABLES
# ========================

param (
    [Parameter(Mandatory = $true)]
    [string]$SRC_DIR,

    [Parameter(Mandatory = $true)]
    [string]$BUILD_DIR,

    [Parameter(Mandatory = $true)]
    [string]$INSTALL_DIR,

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

if (-Not (Test-Path $INSTALL_DIR)) {
    Write-Host " Install dir not found at: $INSTALL_DIR. Making new one.." -ForegroundColor Yellow
    New-Item -Path $INSTALL_DIR -ItemType Directory -Force
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
# $flags = Get-Content $SRC_DIR"\tools\build\freecad_flags.txt"
# # Pattern to match LibPack path (escaped for regex)
# $libpackPattern = "C:/archi-ve/LibPack-[^/]+(/.+)"
# $toolsPattern = "C:/archi-ve/tools[^/]+(/.+)"
# $msvcPattern = "C:/Program Files/Microsoft Visual Studio/2022/Community[^/]+(/.+)"
# # Replace paths
# $updatedFlags = $flags | ForEach-Object {
#     if ($_ -match $libpackPattern -and $_ -notmatch "C:\\archi-ve\\LibPack") {
#         $subpath = $Matches[1] -replace "/", "\"
#         $_ -replace $libpackPattern, "$LIBPACK_DIRECTORY$subpath"
#     } 
#     elseif ($_ -match $toolsPattern -and $_ -notmatch "C:\\archi-ve\\tools") {
#         $subpath = $Matches[1] -replace "/", "\"
#         $_ -replace $toolsPattern, "$TOOLS_DIRECTORY$subpath"
#     } 
#     elseif ($_ -match $msvcPattern -and $_ -notmatch "C:\\Program Files\\Microsoft Visual Studio") {
#         $subpath = $Matches[1] -replace "/", "\"
#         $_ -replace $msvcPattern, "$VS2022_DIRECTORY$subpath"
#     } 
#     else {
#         $_
#     }
# }
# $updatedFlags | Set-Content "$SRC_DIR\tools\build\final_flags.txt"

Push-Location $SRC_DIR
Write-Host "Starting CMake configuration..." -ForegroundColor Green
$cmakePath = Join-Path $TOOLS_DIRECTORY "\cmake\bin\cmake.exe"
$cmakeArgs = @(
    '-G', 'Visual Studio 17 2022',
    '-DCMAKE_BUILD_TYPE=Release',
    "-DFREECAD_LIBPACK_DIR=$LIBPACK_DIRECTORY",
    "-DCMAKE_PREFIX_PATH=$LIBPACK_DIRECTORY",
    "-DCMAKE_INSTALL_PREFIX=$INSTALL_DIR",
    '-DCMAKE_POLICY_VERSION_MINIMUM="3.5"',
    '-DBUILD_TEST=OFF',
    '-DFREECAD_BUILD_TEST=OFF',
    '-S', $SRC_DIR,
    '-B', $BUILD_DIR
)

$cmakeOutput = & $cmakePath $cmakeArgs

# Save logs to a file for reference
$logFile = "$BUILD_DIR\cmake_execution.log"
$cmakeOutput | Set-Content $logFile

# Search for errors in the logs


$errorLines = $cmakeOutput | Select-String -Pattern "(?i)error"

if ($errorLines) {
    Write-Host "CMake Output:" -ForegroundColor Cyan
    $cmakeOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Errors found during execution:" -ForegroundColor Red
    $errorLines | ForEach-Object { Write-Host $_ -ForegroundColor Red }
    exit 1
} else {
    Write-Host "Execution completed successfully." -ForegroundColor Green
}


  
Pop-Location
# Optional: build
# cmake --build $BUILD_DIR --config Release --parallel
