@echo off
REM Set variables
set "TAR_WORKING_DIR=src"
set "TAR_TARGET_DIR=plugin.video.dropout.tv"
set "ZIP_NAME=plugin.video.dropout.tv.zip"
set "TEMP_ZIP=%TEMP%\%ZIP_NAME%"
set "USER_DIR_ZIP_NAME=%USERPROFILE%\%ZIP_NAME%"

REM Remove old temp zip if exists
if exist "%TEMP_ZIP%" del /f /q "%TEMP_ZIP%"

REM Create zip
tar -a -c -C "%TAR_WORKING_DIR%" -f "%TEMP_ZIP%" "%TAR_TARGET_DIR%"

REM Remove old zip in USER DIR if exists
if exist "%USER_DIR_ZIP_NAME%" del /f /q "%USER_DIR_ZIP_NAME%"

REM Move the zip to user's home directory
move /y "%TEMP_ZIP%" "%USER_DIR_ZIP_NAME%"

echo "Zip created at: %USER_DIR_ZIP_NAME%"
echo "Note that KODI caches the filesystem access"
echo "This means install plugin from 'zip' requires a KODI restart after each change of the zip file..."
pause
