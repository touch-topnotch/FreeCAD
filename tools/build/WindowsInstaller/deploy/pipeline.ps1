# the perfect directory should be like
# path/to/archi-ve/
# ----> FreeCAD (from github)
# ----> LibPack (from github)
# ----> tools (from google drive)
# C:/Program Files/Microsoft Visual Studio/2022/Community

$SRC_DIR = "D:\GOIDA\FreeCAD"
$BUILD_DIR = "D:\GOIDA\FreeCAD\build"
$TOOLS_DIR = "D:\GOIDA\tools"
$LIBPACK_DIRECTORY = "D:\GOIDA\LibPack-1.1.0-v3.1.0-Release"
$VS2022_DIRECTORY = "C:\Program Files\Microsoft Visual Studio\2022\Community"

Write-Host "===== Setting up environment for Telegram notifications ====="
$CONFIGURE_BUILD = $false
$INSTALL_BUILD   = $false
$MAKE_INSTALLER  = $true
$SEND_INSTALLER  = $true
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

function Send-TelegramFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath
    )

    # ---------------------------------------------------------------------------
    #  Replace with your actual Telegram Bot Token and Chat ID
    # ---------------------------------------------------------------------------
    $BotToken = "7604470857:AAGepgWkFWSi_qqZUW-wJXA9O9axf2vC6F0"
    $ChatID   = "1042330275"
    # ---------------------------------------------------------------------------

    $Url = "https://api.telegram.org/bot$($BotToken)/sendDocument"

    try {
        # Prepare the multipart form-data content
        $boundary = [System.Guid]::NewGuid().ToString()
        $headers = @{
            "Content-Type" = "multipart/form-data; boundary=$boundary"
        }
        $body = @"
--$boundary
Content-Disposition: form-data; name="chat_id"

$ChatID
--$boundary
Content-Disposition: form-data; name="document"; filename="$(Split-Path -Leaf $FilePath)"
Content-Type: application/octet-stream

$(Get-Content -Path $FilePath -Raw)
--$boundary--
"@

        # Send the request
        Invoke-RestMethod -Uri $Url -Method Post -Headers $headers -Body $body
    }
    catch {
        Write-Host "ERROR sending file to Telegram: $_"
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

    if ($LASTEXITCODE -eq 0) {
        Send-TelegramMessage "Configuration done"
    } else {

        $telegramMessage = @(
        "Configuration part failed. Here is a log file:"
        ) -join "`n"

        Send-TelegramMessage $telegramMessage
        Send-TelegramFile "$BUILD_DIR\cmake_execution.log"
        Exit 1
    }


}
# ------------------------------------------------------------------------------
# 3) Run build_install.ps1
# ------------------------------------------------------------------------------

if($INSTALL_BUILD)
{
    Write-Host "===== Running install_build.ps1 =====" -ForegroundColor Green
    
    # Create log files in advance
    $buildLog = "$BUILD_DIR\install_build.log"
    $errorLog = "$BUILD_DIR\install_build_error.log"
    "" | Set-Content $buildLog
    "" | Set-Content $errorLog

    try {
        # Start process with elevated privileges
        $process = Start-Process powershell -Verb RunAs -ArgumentList "-ExecutionPolicy", "Bypass", "-File", "`"$PSScriptRoot\install_build.ps1`"", "`"$BUILD_DIR`"", "`"$VS2022_DIRECTORY`"" -Wait -PassThru
        
        if ($process.ExitCode -eq 0) {
            Write-Host "Build completed successfully" -ForegroundColor Green
            Send-TelegramMessage "Compilation done"
        } else {
            Write-Host "Build failed with error code: $($process.ExitCode)" -ForegroundColor Red
            
            $telegramMessage = @(
                "Installation build part failed. Error code: $($process.ExitCode)",
                "Check logs for details."
            ) -join "`n"
            
            Send-TelegramMessage $telegramMessage
            
            # Send logs only if they exist and not empty
            if (Test-Path $buildLog) {
                $content = Get-Content $buildLog
                if ($content.Length -gt 0) {
                    Send-TelegramFile $buildLog
                }
            }
            if (Test-Path $errorLog) {
                $content = Get-Content $errorLog
                if ($content.Length -gt 0) {
                    Send-TelegramFile $errorLog
                }
            }
            
            Exit 1
        }
    }
    catch {
        Write-Host "Error launching process: $_" -ForegroundColor Red
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
    $SRC_DIR"\tools\build\WindowsInstaller\FreeCAD-installer.nsi" `
    $VS2022_DIRECTORY `

    if ($LASTEXITCODE -eq 0) {
        Send-TelegramMessage "Making installer done"
    } else {
     $errorMessage = $output -join "`n"

       
        $telegramMessage = @(
        "Installation build part failed. Here is a log file:"
        ) -join "`n"

        Send-TelegramMessage $telegramMessage
        Send-TelegramFile $SRC_DIR"\tools\build\WindowsInstaller\make_installer.log"
        Exit 1
    }
}
# ------------------------------------------------------------------------------
# 5) Run send_installer_to_server.ps1
# ------------------------------------------------------------------------------
if($SEND_INSTALLER){

    echo "===== Running send_installer_to_server.ps1 ====="
    Write-Host "===== Running send_installer_to_server.ps1 ====="

    # Define the installer folder path
    $installerDir = Join-Path $SRC_DIR "tools\build\windowsinstaller"

    # Search for the first .exe file that contains "Archi" in its name
    $exeFile = Get-ChildItem -Path $installerDir -Filter "*installer*.exe" -File | Select-Object -First 1

    if ($exeFile) {
        $newPath = Join-Path $installerDir "\ArchiSetup.exe"
        Rename-Item -Path $exeFile.FullName -NewName $newPath -Force
        Write-Host " Renamed '$($exeFile.Name)' to 'ArchiSetup.exe'"
    } else {
        Write-Host "No EXE file containing 'Archi' found in: $installerDir" -ForegroundColor Red
        Send-TelegramMessage "No EXE file containing 'Archi' found in: $installerDir"
        Exit(1)
    }


powershell -ExecutionPolicy Bypass -File "./send_installer_to_server.ps1" `
    "$newPath" `
    "hKG+*52pXCxp" `
    "89.169.36.93" `
    "/../var/www/archi-website/apps" `
    "root" `
    "$TOOLS_DIR"

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