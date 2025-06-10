# Установка Chocolatey (если ещё нет)
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Установка SSH (OpenSSH)
choco install -y openssh
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'
#Requires -RunAsAdministrator
$ErrorActionPreference = 'Stop'
$gitVersion   = '2.49.0'   # latest as of 2025-03-17  [oai_citation:2‡git-scm.com](https://git-scm.com/downloads/win?utm_source=chatgpt.com)
$gitExe       = "Git-$gitVersion-64-bit.exe"
$tempExe      = Join-Path $env:TEMP $gitExe
$downloadUri  = "https://github.com/git-for-windows/git/releases/download/v$gitVersion.windows.1/$gitExe"

Write-Host "1. Remove any old Git:"
choco uninstall git -n -y --skip-autouninstaller 2>$null
choco uninstall git.install -n -y --skip-autouninstaller 2>$null
Remove-Item "$env:ProgramData\chocolatey\lib\git*" -Recurse -Force -EA SilentlyContinue

Write-Host "2. Try Chocolatey:"
try {
    choco install git -y --force --params "'/GitAndUnixToolsOnPath /NoAutoCrlf'"
    return   # success, we're done
}
catch {
    Write-Warning "Chocolatey failed, switching to manual download..."
}

Write-Host "3. Manual download:"
for ($i=1; $i -le 3; $i++) {
    try {
        if (Test-Path $tempExe) { 
            Get-Process -Name $gitExe -ErrorAction SilentlyContinue | Stop-Process -Force
            Remove-Item $tempExe -Force
        }
        Invoke-WebRequest -Uri $downloadUri -OutFile $tempExe -UseBasicParsing
        break
    }
    catch {
        if ($i -eq 3) { throw "Download failed after 3 attempts" }
        Start-Sleep 5
    }
}

Write-Host "4. Silent install:"
$innosetupArgs = @(
    '/VERYSILENT','/NORESTART','/NOCANCEL','/SP-',
    '/COMPONENTS="icons,assoc,assoc_sh,ext,ext\shellhere,ext\guihere,gitlfs,icons\quicklaunch"'
) -join ' '

Start-Process -FilePath $tempExe -ArgumentList $innosetupArgs -Wait -PassThru |
    ForEach-Object {
        if ($_.ExitCode -ne 0) { throw "Installer exited $($_.ExitCode)" }
    }

Write-Host "Git $gitVersion installed successfully."
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

