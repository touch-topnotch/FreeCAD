

# the perfect directory should be like
# path/to/archi-ve/
# ----> FreeCAD (from github)
# ----> LibPack (from github)
# ----> tools (from google drive)
# C:/Program Files/Microsoft Visual Studio/2022/Community

$SRC_DIR = "C:\archi-ve\FreeCAD"
$BUILD_DIR = "C:\archi-ve\FreeCAD\build"
$TOOLS_DIR = "C:\archi-ve\tools"
$LIBPACK_DIRECTORY = "C:\archi-ve\LibPack-1.1.0-v3.1.0-Release"
$VS2022_DIRECTORY = "C:\Program Files\Microsoft Visual Studio\2022\Community"

Write-Host "===== Setting up environment for Telegram notifications ====="
$CONFIGURE_BUILD = $true
$INSTALL_BUILD   = $false
$MAKE_INSTALLER  = $false
$SEND_INSTALLER  = $false
# Install python-telegram-bot via pip.
# (Assumes Python + pip are already installed on the system)

function Send-TelegramMessage {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    # ---------------------------------------------------------------------------
    #  Replace with your actual Telegram Bot Token and Chat ID
    # ---------------------------------------------------------------------------
    $BotToken = "7604470857:AAGepgWkFWSi_qqZUW-wJXA9O9axf2vC6F0"
    $ChatID   = "1042330275"
    # ---------------------------------------------------------------------------

    $Url = "https://api.telegram.org/bot$($BotToken)/sendMessage"
    $Params = @{
        chat_id    = $ChatID
        text       = $Message
        parse_mode = "Markdown"
    }

    try {
        Invoke-RestMethod -Uri $Url -Method POST -Body $Params
    }
    catch {
        Write-Host "ERROR sending to Telegram: $_"
    }
}


# ------------------------------------------------------------------------------
# 1) Notify start of deployment
# ------------------------------------------------------------------------------
$steps = @(
    "Starting deployment...",
    "CONFIGURE BUILD - $CONFIGURE_BUILD",
    "INSTALL BUILD   - $INSTALL_BUILD",
    "MAKE INSTALLER  - $MAKE_INSTALLER",
    "SEND INSTALLER  - $SEND_INSTALLER"
)

# Output to Telegram (join into a single string)
Send-TelegramMessage ($steps -join "`n")

# ------------------------------------------------------------------------------
# 2) Run compile_cmake.ps1
# ------------------------------------------------------------------------------

if($CONFIGURE_BUILD)
{
    Write-Host "===== Running configure_build.ps1 ====="
    powershell -ExecutionPolicy Bypass -File "./configure_build.ps1" `
    $SRC_DIR `
    $BUILD_DIR `
    $LIBPACK_DIRECTORY `
    $TOOLS_DIR `
    $VS2022_DIRECTORY `

    if ($LASTEXITCODE -eq 0 -and $output -and $output.Count -gt 0 -and ($output[-1] -like "*Generating done*")) {
        Send-TelegramMessage "Configuration done"
    } else {
        $errorMessage = $output -join "`n"

        if ($errorMessage.Length -gt 4000) {
            $errorMessage = ($output | Select-Object -First 40) -join "`n" + "`n...[truncated]"
        }

        $telegramMessage = @(
            "Configuration failed."
        ) -join "`n"

        Send-TelegramMessage $telegramMessage
        Exit 1
    }


}
# ------------------------------------------------------------------------------
# 3) Run build_install.ps1
# ------------------------------------------------------------------------------

if($INSTALL_BUILD)
{
    Write-Host "===== Running install_build.ps1 ====="
    Start-Process powershell -Verb RunAs -ArgumentList '-ExecutionPolicy Bypass -File "./install_build.ps1" `
    $BUILD_DIR `
    $VS2022_DIRECTORY `'

    if ($LASTEXITCODE -eq 0) {
        Send-TelegramMessage "Compilation done"
    } else {
    $errorMessage = $output -join "`n"

        if ($errorMessage.Length -gt 4000) {
            $errorMessage = ($output | Select-Object -First 40) -join "`n" + "`n...[truncated]"
        }

        $telegramMessage = @(
            'Compilation failed:',
            '```powershell',
            $errorMessage,
            '```'
        ) -join "`n"

        Send-TelegramMessage $telegramMessage
        Exit 1
    }
}
# ------------------------------------------------------------------------------
# 4) Run make_installer_nsis.ps1
# ------------------------------------------------------------------------------
if($MAKE_INSTALLER){
    Write-Host "===== Running make_installer_nsis.ps1 ====="
    powershell -ExecutionPolicy Bypass -File "./make_installer.ps1" `
    $TOOLS_DIR"\NSIS\makensis.exe" `
    $SRC_DIR"\tools\build\WindowsInstaller\FreeCAD-installer.nsi"

    if ($LASTEXITCODE -eq 0) {
        Send-TelegramMessage "Making installer done"
    } else {
    $errorMessage = $output -join "`n"

        if ($errorMessage.Length -gt 4000) {
            $errorMessage = ($output | Select-Object -First 40) -join "`n" + "`n...[truncated]"
        }

        $telegramMessage = @(
            'Compilation failed:',
            '```powershell',
            $errorMessage,
            '```',
            'penis'
        ) -join "`n"

        Send-TelegramMessage $telegramMessage
        Exit 1
    }
}
# ------------------------------------------------------------------------------
# 5) Run send_installer_to_server.ps1
# ------------------------------------------------------------------------------
if($SEND_INSTALLER){
    Write-Host "===== Running send_installer_to_server.ps1 ====="

    # Define the installer folder path
    $installerDir = Join-Path $SRC_DIR "tools\build\windowsinstaller"

    # Search for the first .exe file that contains "Archi" in its name
    $exeFile = Get-ChildItem -Path $installerDir -Filter "*Archi*.exe" -File | Select-Object -First 1

    if ($exeFile) {
        $newPath = Join-Path $installerDir "\ArchiSetup.exe"
        Rename-Item -Path $exeFile.FullName -NewName $newPath -Force
        Write-Host " Renamed '$($exeFile.Name)' to 'ArchiSetup.exe'"
    } else {
        Write-Host "No EXE file containing 'Archi' found in: $installerDir" -ForegroundColor Red
        Send-TelegramMessage "No EXE file containing 'Archi' found in: $installerDir"
    }


    powershell -ExecutionPolicy Bypass -File "./send_installer_to_server.ps1" `
    -FilePath $installerDir"\ArchiSetup.exe" `
    -Password "hKG+*52pXCxp" 

    if ($LASTEXITCODE -eq 0) {
        Send-TelegramMessage "Installer sent"
    } else {
        $errorMessage = $output -join "`n"

        if ($errorMessage.Length -gt 4000) {
            $errorMessage = ($output | Select-Object -First 2000) -join "`n" + "`n...[truncated]"
        }
        

        $telegramMessage = @(
            'Compilation failed:',
            '```powershell',
            $errorMessage,
            '```'
        ) -join "`n"

        Send-TelegramMessage $telegramMessage
        Exit 1
    }
}
# ------------------------------------------------------------------------------
# 6) Final message
# ------------------------------------------------------------------------------
Send-TelegramMessage "Deployment Done!"

Write-Host "===== Pipeline finished successfully! ====="