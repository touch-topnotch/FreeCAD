# Установка Chocolatey (если ещё нет)
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Установка SSH (OpenSSH)
choco install -y openssh
# Install Microsoft’s own OpenSSH server bits
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Start and enable the service
Start-Service sshd
Set-Service -Name sshd -StartupType Automatic
# Install vdagent for remote access
choco install -y spice-vdagent
Start-Service spice-vdagent
Set-Service -Name spice-vdagent -StartupType Automatic

# Установка Conda + Mamba
choco install -y miniconda3
conda install -n base -y -c conda-forge mamba

# Установка Visual Studio 2022 (Community)
choco install -y visualstudio2022community --package-parameters="--add Microsoft.VisualStudio.Workload.Azure --add Microsoft.VisualStudio.Workload.NetWeb --add Microsoft.VisualStudio.Workload.Data --quiet --norestart --wait"

# Создание папки для репозиториев
New-Item -ItemType Directory -Force -Path "C:\repos"

# Клонирование репозиториев (замените ссылки на свои)
git clone https://github.com/touch-topnotch/FreeCAD C:\Users\Administrator\archi-ve\FreeCAD
git checkout dev
git clone https://github.com/touch-topnotch/ArchiModule C:\Users\Administrator\archi-ve\FreeCAD\src\Mod\ArchiModule

# Готово!
Write-Host "✅ Всё установлено! Активируем environment"

# Initialize and activate conda/mamba environment
Write-Host "Initializing conda and activating base environment..."
$condaPath = "C:\Users\Administrator\miniconda3"
$condaInitScript = "$condaPath\shell\condabin\conda-hook.ps1"

# Initialize conda for PowerShell
if (Test-Path $condaInitScript) {
    . $condaInitScript
    conda activate base
    Write-Host "✅ Conda base environment activated"
} else {
    Write-Warning "Conda initialization script not found at $condaInitScript"
}

# Configure VS Code settings
Write-Host "Configuring VS Code settings..."
$vscodeSettingsPath = "C:\Users\Administrator\archi-ve\freecad\.vscode"
$vscodeSettingsFile = "$vscodeSettingsPath\settings.json"

# Create .vscode directory if it doesn't exist
New-Item -ItemType Directory -Force -Path $vscodeSettingsPath

# Create settings.json with the specified configuration
$settingsJson = @{
    "terminal.integrated.profiles.windows" = @{
        "VsDevCmd (2022)" = @{
            "path" = @(
                "C:\\Windows\\Sysnative\\cmd.exe",
                "C:\\Windows\\System32\\cmd.exe"
            )
            "args" = @(
                "/k",
                "C:/Program Files/Microsoft Visual Studio/2022/Community/Common7/Tools/VsDevCmd.bat",
                "-arch=x64",
                "-host_arch=x64"
            )
            "overrideName" = $true
            "icon" = "terminal-cmd"
        }
    }
} | ConvertTo-Json -Depth 10

# Write settings to file
Set-Content -Path $vscodeSettingsFile -Value $settingsJson

Write-Host "✅ VS Code settings configured successfully!"

