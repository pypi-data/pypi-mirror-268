@echo off
setlocal enabledelayedexpansion

:: Define paths
set "source_folder=C:\MEDIANSI\MediCare"
set "target_folder=C:\MEDIANSI\MediCare\CSV"
set "config_file=F:\Medibot\json\config.json"
set "python_script=C:\Python34\Lib\site-packages\MediBot\update_json.py"
set "python_script2=C:\Python34\Lib\site-packages\MediBot\Medibot.py"
set "medicafe_package=medicafe"
set "upgrade_medicafe=F:\Medibot\upgrade_medicafe.py"

:: Set PYTHONWARNINGS environment variable to ignore deprecation warnings
set PYTHONWARNINGS=ignore

:: Upgrade Medicafe package
py "%upgrade_medicafe%"

:: Check for the latest CSV file in source folder
set "latest_csv="
for /f "delims=" %%a in ('dir /b /a-d /o-d "%source_folder%\*.csv" 2^>nul') do (
    set "latest_csv=%%a"
    goto :found_latest_csv
)

:: If no CSV found in source folder, check target folder
echo No CSV file found in "%source_folder%".
for /f "delims=" %%a in ('dir /b /a-d /o-d "%target_folder%\*.csv" 2^>nul') do (
    set "latest_csv=%%a"
    echo Using latest processed file in CSV folder: !latest_csv!
    goto :found_latest_csv
)

:found_latest_csv

:: If no CSV found in either folder, end the script
if not defined latest_csv (
    echo No CSV file found in either folder.
    goto :end_script
)

:: Display the name of the found CSV file to the user
echo Found CSV file: !latest_csv!

:: Get the current date in MMDDYY format
for /f "tokens=1-3 delims=/" %%a in ("%date%") do (
    set "month=%%a"
    set "day=%%b"
    set "year=%%c"
)
set "datestamp=!month!!day!!year:~2,2!"

:: Move and rename the CSV file only if found in source folder
if exist "%source_folder%\!latest_csv!" (
    move "%source_folder%\!latest_csv!" "%target_folder%\SX_CSV_!datestamp!.csv"
    set "new_csv_path=%target_folder%\SX_CSV_!datestamp!.csv"
) else (
    set "new_csv_path=%target_folder%\!latest_csv!"
)

echo Please wait...

:: Call Python script to update the JSON file
py "%python_script%" "%config_file%" "!new_csv_path!"

:: Execute the second Python script
py "%python_script2%" "%config_file%"

:end_script
pause
