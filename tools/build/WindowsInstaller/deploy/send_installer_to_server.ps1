param (
    [string]$FilePath = "C:\path\to\your\file.zip",
    [string]$Password = "your_password_here",
    [string]$FtpServer = "89.169.36.93",
    [string]$RemotePath = "~/../var/www/archi-website/apps",  # subfolder relative to FTP home
    [string]$Username = "root"
)

# Extract filename
$FileName = [System.IO.Path]::GetFileName($FilePath)
$ftpUri = "ftp://$FtpServer/$RemotePath/$FileName"

# Create WebClient and upload file
$webclient = New-Object System.Net.WebClient
$webclient.Credentials = New-Object System.Net.NetworkCredential($Username, $Password)

try {
    Write-Host "Uploading $FilePath to $ftpUri..."
    $webclient.UploadFile($ftpUri, "STOR", $FilePath)
    Write-Host "✅ Upload complete!"
} catch {
    Write-Host " Upload failed: $_" -ForegroundColor Red
    exit 1
}
