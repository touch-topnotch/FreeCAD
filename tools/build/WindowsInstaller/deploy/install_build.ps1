param (
    [Parameter(Mandatory = $true)]
    [string]$BUILD_DIR,

    [Parameter(Mandatory = $true)]
    [string]$VS2022_DIRECTORY
)

Write-Host "Starting install_build.ps1..." -ForegroundColor Green

# Check if build directory exists
if (-Not (Test-Path $BUILD_DIR)) {
    Write-Host "Build directory not found: $BUILD_DIR" -ForegroundColor Red
    exit 1
}

# Check if Visual Studio exists
if (-Not (Test-Path $VS2022_DIRECTORY)) {
    Write-Host "Visual Studio 2022 not found: $VS2022_DIRECTORY" -ForegroundColor Red
    exit 1
}

try {
    # Import Visual Studio environment variables
    $vcvarsall = Join-Path $VS2022_DIRECTORY "VC\Auxiliary\Build\vcvarsall.bat"
    if (-Not (Test-Path $vcvarsall)) {
        Write-Host "vcvarsall.bat not found: $vcvarsall" -ForegroundColor Red
        exit 1
    }

    Write-Host "Creating temporary build batch file..." -ForegroundColor Yellow
    # Create temporary batch file for VS environment setup and build
    $tempBatch = Join-Path $BUILD_DIR "temp_build.bat"
    @"
@echo on
echo Starting Visual Studio environment setup...
call "$vcvarsall" x64
if errorlevel 1 (
    echo Error: Failed to setup Visual Studio environment
    exit /b 1
)

echo Starting CMake build...
cmake --build "$BUILD_DIR" --config Release --target install --parallel
if errorlevel 1 (
    echo Error: Build failed
    exit /b 2
)

echo Build completed successfully
exit /b 0
"@ | Set-Content $tempBatch -Encoding ASCII

    # Start build
    Write-Host "Starting Release configuration build..." -ForegroundColor Yellow
    
    # Run cmd.exe directly for better output
    $buildProcess = Start-Process cmd.exe -ArgumentList "/c", "`"$tempBatch`" 2>&1" -NoNewWindow -Wait -PassThru
    
    # Check result
    if ($buildProcess.ExitCode -ne 0) {
        Write-Host "Build failed. Exit code: $($buildProcess.ExitCode)" -ForegroundColor Red
        exit $buildProcess.ExitCode
    }

    Write-Host "Build completed successfully!" -ForegroundColor Green
    exit 0
}
catch {
    Write-Host "Error occurred during build process: $_" -ForegroundColor Red
    exit 1
}
finally {
    # Cleanup temporary files
    if (Test-Path $tempBatch) {
        Remove-Item $tempBatch -Force
    }
}
