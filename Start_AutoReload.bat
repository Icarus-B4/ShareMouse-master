@echo off
cd /d "%~dp0"
echo Starting ShareMouse Auto-Reload...
echo This window must stay open. Minimize it to keep it running.
python sharemouse_windows.py
pause
