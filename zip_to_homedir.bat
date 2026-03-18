@echo off
REM Set variables
set "SOURCE_DIR=plugin\plugin.video.dropout.tv"
set "ZIP_NAME=plugin.video.dropout.tv.zip"
set "TEMP_ZIP=%TEMP%\%ZIP_NAME%"
set "USER_DIR_ZIP_NAME=%USERPROFILE%\%ZIP_NAME%"

REM Remove old temp zip if exists
if exist "%TEMP_ZIP%" del /f /q "%TEMP_ZIP%"

REM Create zip using PowerShell
powershell -Command "Compress-Archive -Path '%SOURCE_DIR%' -DestinationPath '%TEMP_ZIP%' -Force"

REM Remove old zip in USER DIR if exists
if exist "%USER_DIR_ZIP_NAME%" del /f /q "%USER_DIR_ZIP_NAME%"

REM Move the zip to user's home directory
move /y "%TEMP_ZIP%" "%USER_DIR_ZIP_NAME%"

echo "Zip created at: %USER_DIR_ZIP_NAME%"
pause
