# Установка Chocolatey (если ещё нет)
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Установка SSH (OpenSSH)
choco install -y openssh
# Install Microsoft's own OpenSSH server bits
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Start and enable the service
Start-Service sshd
Set-Service -Name sshd -StartupType Automatic


# Установка Conda + Mamba
choco install -y miniconda3
# Установка Conda + Mamba
$minicondaPath = "C:\Users\Administrator\miniconda3"
$minicondaInstaller = Join-Path $env:TEMP "Miniconda3-latest-Windows-x86_64.exe"
$minicondaScriptsPath = "$minicondaPath\Scripts"
$minicondaLibraryPath = "$minicondaPath\Library\bin"

# Download and install Miniconda if not already installed
if (-not (Test-Path $minicondaPath)) {
    Write-Host "Downloading Miniconda installer..."
    try {
        Invoke-WebRequest -Uri "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe" -OutFile $minicondaInstaller -UseBasicParsing
        
        Write-Host "Installing Miniconda..."
        Start-Process -FilePath $minicondaInstaller -ArgumentList "/S /RegisterPython=1 /AddToPath=1 /InstallationType=JustMe /D=$minicondaPath" -Wait -NoNewWindow
        
        # Clean up installer
        Remove-Item $minicondaInstaller -Force
    } catch {
        Write-Error "Failed to install Miniconda: $_"
        exit 1
    }
}

# Add to system PATH
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
if (-not $currentPath.Contains($minicondaPath)) {
    [Environment]::SetEnvironmentVariable("Path", "$currentPath;$minicondaPath;$minicondaScriptsPath;$minicondaLibraryPath", "User")
    # Refresh current session's PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "User")
}

# Initialize conda for PowerShell
$condaInitScript = "$minicondaPath\shell\condabin\conda-hook.ps1"
if (Test-Path $condaInitScript) {
    . $condaInitScript
    & "$minicondaPath\Scripts\conda.exe" init powershell
    Write-Host "Conda has been initialized. Please restart your PowerShell session to use conda commands."
} else {
    Write-Error "Conda initialization script not found at: $condaInitScript"
    exit 1
}


# Create a batch file to initialize conda in cmd
$condaInitCmd = @"
@echo off
call "$minicondaPath\Scripts\activate.bat"
"@
$condaInitCmd | Out-File -FilePath "$minicondaPath\Scripts\conda-init.cmd" -Encoding ASCII

Write-Host "Conda has been added to system PATH. Please restart your computer for changes to take effect."
conda install -n base -y -c conda-forge mamba

# Установка Visual Studio 2022 (Community)
choco install -y visualstudio2022community --package-parameters="--add Microsoft.VisualStudio.Workload.NativeDesktop --quiet --norestart --wait"

# Создание папки для репозиториев
New-Item -ItemType Directory -Force -Path "C:\repos"

# Клонирование репозиториев (замените ссылки на свои)
git clone https://github.com/touch-topnotch/FreeCAD C:\Users\Administrator\archi-ve\FreeCAD
git checkout dev
git submodule update --init --recursive
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
# Install pixi package manager
Write-Host "Installing pixi package manager..."
$pixiInstaller = Join-Path $env:TEMP "pixi-installer.exe"

try {
    # Download pixi installer
    Invoke-WebRequest -Uri "https://pixi.sh/install.ps1" -OutFile $pixiInstaller -UseBasicParsing
    
    # Run the installer with explicit architecture specification
    Start-Process -FilePath $pixiInstaller -ArgumentList "--arch", "x64" -Wait -NoNewWindow
    
    # Clean up installer
    Remove-Item $pixiInstaller -Force
    
    Write-Host "✅ Pixi installed successfully!"
} catch {
    Write-Error "Failed to install pixi: $_"
    exit 1
}
