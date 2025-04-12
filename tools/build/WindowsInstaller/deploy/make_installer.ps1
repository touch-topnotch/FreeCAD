param (
    [Parameter(Mandatory = $true)]
    [string]$MakensisPath,

    [Parameter(Mandatory = $true)]
    [string]$NsiScriptPath
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

# Run makensis with LZMA compressor
& "$MakensisPath" /V4 /DCompress=LZMA "$NsiScriptPath"

# Exit with status
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ NSIS installer built successfully." -ForegroundColor Green
} else {
    Write-Host " NSIS build failed with exit code $LASTEXITCODE." -ForegroundColor Red
}
