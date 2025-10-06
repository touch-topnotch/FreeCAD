param (
    [string]$FilePath = "C:\archi-ve\FreeCAD\tools\build\WindowsInstaller\ArchiSetup.exe",
    [string]$Password = "your_password_here",
    [string]$SshServer = "89.169.36.93",
    [string]$RemotePath = "/var/www/archi-website/apps",  # Must exist on the server
    [string]$Username = "root",
    [string]$TOOLS_DIR = "C:\archi-ve\tools"
)

Write-Host "Starting file transfer process..." -ForegroundColor Yellow

# Check if file exists
if (-not (Test-Path $FilePath)) {
    Write-Host "Error: Source file not found: $FilePath" -ForegroundColor Red
    exit 1
}

# Check if pscp exists
$pscpPath = Join-Path $TOOLS_DIR "\pscp.exe"
if (-not (Test-Path $pscpPath)) {
    Write-Host "Error: pscp.exe not found at: $pscpPath" -ForegroundColor Red
    exit 1
}

# Test server connectivity
Write-Host "Testing server connectivity..." -ForegroundColor Yellow
$pingResult = Test-Connection -ComputerName $SshServer -Count 1 -Quiet
if (-not $pingResult) {
    Write-Host "Error: Cannot reach server $SshServer. Please check network connectivity and firewall settings." -ForegroundColor Red
    exit 1
}

# Test SSH port
Write-Host "Testing SSH port (22)..." -ForegroundColor Yellow
$tcpTest = Test-NetConnection -ComputerName $SshServer -Port 22 -WarningAction SilentlyContinue
if (-not $tcpTest.TcpTestSucceeded) {
    Write-Host "Error: Cannot connect to SSH port (22) on $SshServer" -ForegroundColor Red
    Write-Host "Possible issues:" -ForegroundColor Yellow
    Write-Host "1. SSH service is not running on the server" -ForegroundColor Yellow
    Write-Host "2. Port 22 is blocked by firewall" -ForegroundColor Yellow
    Write-Host "3. Server's SSH configuration is incorrect" -ForegroundColor Yellow
    Write-Host "`nTroubleshooting steps:" -ForegroundColor Cyan
    Write-Host "1. Contact server administrator to verify SSH service is running" -ForegroundColor Cyan
    Write-Host "2. Check if you can connect using: ssh $Username@$SshServer" -ForegroundColor Cyan
    Write-Host "3. Verify firewall rules allow outbound connections to port 22" -ForegroundColor Cyan
    exit 1
}

# Construct destination properly using ${} for variables with special characters
$destination = "${Username}@${SshServer}:${RemotePath}/$(Split-Path $FilePath -Leaf)"

Write-Host "Sending file to server..." -ForegroundColor Yellow
Write-Host "Source: $FilePath" -ForegroundColor Gray
Write-Host "Destination: $destination" -ForegroundColor Gray

try {
    # Run the command with timeout
    $process = Start-Process -FilePath $pscpPath -ArgumentList "-pw", $Password, "$FilePath", "$destination" -Wait -NoNewWindow -PassThru
    
    if ($process.ExitCode -eq 0) {
        Write-Host "File transfer completed successfully!" -ForegroundColor Green
        exit 0
    } else {
        Write-Host "Error: File transfer failed with exit code $($process.ExitCode)" -ForegroundColor Red
        Write-Host "Please check:" -ForegroundColor Yellow
        Write-Host "1. Server is running and accessible" -ForegroundColor Yellow
        Write-Host "2. SSH port (22) is open and not blocked by firewall" -ForegroundColor Yellow
        Write-Host "3. Username and password are correct" -ForegroundColor Yellow
        Write-Host "4. Remote directory exists and is writable" -ForegroundColor Yellow
        exit 1
    }
}
catch {
    Write-Host "Error during file transfer: $_" -ForegroundColor Red
    exit 1
}