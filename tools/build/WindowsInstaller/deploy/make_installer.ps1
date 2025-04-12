param (
    [Parameter(Mandatory = $true)]
    [string]$MakensisPath,

    [Parameter(Mandatory = $true)]
    [string]$NsiScriptPath,

    [Parameter(Mandatory = $true)]
    [string]$VS2022_DIRECTORY
)


# Validate NSIS compiler path
if (-Not (Test-Path $MakensisPath)) {
    Write-Host " NSIS compiler not found at: $MakensisPath" -ForegroundColor Red
    exit 1
}

# Validate NSI script path
if (-Not (Test-Path $NsiScriptPath)) {
    Write-Host " NSIS script not found at: $NsiScriptPath" -ForegroundColor Red
    exit 1
}
# Validate NSI script path
if (-Not (Test-Path $VS2022_DIRECTORY)) {
    Write-Host " VS2022 not found at: $VS2022_DIRECTORY" -ForegroundColor Red
    exit 1
}

$msvcRedistPath = $NsiScriptPath -replace "FreeCAD-installer.nsi", "MSVCRedist"
if (-Not (Test-Path $msvcRedistPath)) {
    Write-Host " MSVC Redist not found at: $msvcRedistPath" -ForegroundColor Red
    exit 1
}
# Список всех библиотек и их подкаталогов
$dllMap = @{
    "concrt140.dll"          = "Microsoft.VC143.CRT"
    "msvcp140.dll"           = "Microsoft.VC143.CRT"
    "vccorlib140.dll"        = "Microsoft.VC143.CRT"
    "vcruntime140_1.dll"     = "Microsoft.VC143.CRT"
    "vcomp140.dll"           = "Microsoft.VC143.OpenMP"
    "vcamp140.dll"           = "Microsoft.VC143.CXXAMP"
}

# Базовая директория редистов
$vcRedistBasePath = Join-Path $VS2022_DIRECTORY "VC\Redist\MSVC"

# Находим последнюю версию (самую "свежую" папку)
$latestVersionPath = Get-ChildItem -Path $vcRedistBasePath -Directory |
    Where-Object { $_.Name -like '*.*' } |
    Select-Object -First 1
if (-not $latestVersionPath) {
    Write-Error "Не найдена версия с '.' в $vcRedistBasePath"
    exit 1
}
Write-Host "Selected version path: $($latestVersionPath.FullName)"

# Создаем папку назначения, если она не существует
if (-not (Test-Path $msvcRedistPath)) {
    New-Item -ItemType Directory -Path $msvcRedistPath | Out-Null
}

# Копируем библиотеки из нужных подкаталогов
foreach ($dll in $dllMap.Keys) {
    $subfolder = $dllMap[$dll]
    $sourceDir = Join-Path $latestVersionPath.FullName "x64\$subfolder"
    $sourcePath = Join-Path $sourceDir $dll
    $destPath = Join-Path $msvcRedistPath $dll

    if (Test-Path $sourcePath) {
        Copy-Item -Path $sourcePath -Destination $destPath -Force
        Write-Host "Copied $dll from $subfolder"
    } else {
        Write-Warning "$dll not found in $sourceDir"
    }
}
Write-Host "Starting NSIS build..."
$logFile = Join-Path (Split-Path -Path $NsiScriptPath -Parent) "make_installer.log"
# Run makensis with LZMA compressor
& "$MakensisPath" /V4 /DCompress=LZMA "$NsiScriptPath" > "$logFile" 2>&1

# Exit with status
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ NSIS installer built successfully." -ForegroundColor Green
} else {
    Write-Host " NSIS build failed with exit code $LASTEXITCODE." -ForegroundColor Red
    Exit(1)
}
