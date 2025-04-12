param (
    [string]$FilePath = "C:\archi-ve\FreeCAD\tools\build\WindowsInstaller\ArchiSetup.exe",
    [string]$Password = "your_password_here",
    [string]$SshServer = "89.169.36.93",
    [string]$RemotePath = "/var/www/archi-website/apps",  # Must exist on the server
    [string]$Username = "root",
    [string]$TOOLS_DIR = "C:\archi-ve\tools"
)
Write-Host "Sending file to server..."
# Construct destination properly using ${} for variables with special characters
$destination = "${Username}@${SshServer}:${RemotePath}/$(Split-Path $FilePath -Leaf)"

# Here's a version using 'pscp' from PuTTY suite
$pscpPath = Join-Path $TOOLS_DIR "\pscp.exe"  # Adjust if installed elsewhere

# Run the command
& "$pscpPath" -pw $Password "$FilePath" "$destination"