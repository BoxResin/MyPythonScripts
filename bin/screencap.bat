@echo off

IF NOT "%~2"=="" (
    python "C:\python_scripts\Scripts\screencap.py" %1 %2
) ELSE (IF NOT "%~1"=="" (
    python "C:\python_scripts\Scripts\screencap.py" %1
    )
)