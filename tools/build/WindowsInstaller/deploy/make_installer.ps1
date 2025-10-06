param (
    [Parameter(Mandatory = $true)]
    [string]$MakensisPath,

    [Parameter(Mandatory = $true)]
    [string]$NsiScriptPath,

    [Parameter(Mandatory = $true)]
    [string]$VS2022_DIRECTORY
)

Write-Host "Starting make_installer.ps1..." -ForegroundColor Green

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

# Validate VS2022 directory
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
    "vcruntime140.dll"       = "Microsoft.VC143.CRT"
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
    $sourceDir = Join-Path $latestVersionPath.FullName "x86\$subfolder"
    $sourcePath = Join-Path $sourceDir $dll
    $destPath = Join-Path $msvcRedistPath $dll

    if (Test-Path $sourcePath) {
        Copy-Item -Path $sourcePath -Destination $destPath -Force
        Write-Host "Copied $dll from $subfolder"
    } else {
        Write-Warning "$dll not found in $sourceDir"
    }
}

Write-Host "Starting NSIS build..." -ForegroundColor Yellow

# Create log files
$buildLog = Join-Path (Split-Path -Path $NsiScriptPath -Parent) "make_installer.log"
$errorLog = Join-Path (Split-Path -Path $NsiScriptPath -Parent) "make_installer_error.log"
"" | Set-Content $buildLog
"" | Set-Content $errorLog

try {
    # Create temporary batch file for NSIS build
    $tempBatch = Join-Path (Split-Path -Path $NsiScriptPath -Parent) "temp_nsis_build.bat"
    @"
@echo on
echo Starting NSIS build...
"$MakensisPath" /V4 /DCompress=LZMA "$NsiScriptPath" 2>&1
if errorlevel 1 (
    echo Error: NSIS build failed
    exit /b 1
)
echo NSIS build completed successfully
exit /b 0
"@ | Set-Content $tempBatch -Encoding ASCII

    # Start process and show output
    $process = Start-Process cmd.exe -ArgumentList "/c", "`"$tempBatch`"" -Wait -NoNewWindow -PassThru

    # Check result
    if ($process.ExitCode -eq 0) {
        Write-Host "✅ NSIS installer built successfully." -ForegroundColor Green
        exit 0
    } else {
        Write-Host "❌ NSIS build failed with exit code $($process.ExitCode)." -ForegroundColor Red
        exit 1
    }
}
catch {
    Write-Host "Error occurred during NSIS build process: $_" -ForegroundColor Red
    exit 1
}
finally {
    # Cleanup temporary files
    if (Test-Path $tempBatch) {
        Remove-Item $tempBatch -Force
    }
}
