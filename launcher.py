"""
ShareMouse AutoReload Launcher
Silently launches Start_AutoReload.bat
"""
import subprocess
import sys
import os

def main():
    # Get the directory where this executable is located
    if getattr(sys, 'frozen', False):
        # Running as compiled exe
        script_dir = os.path.dirname(sys.executable)
    else:
        # Running as script
        script_dir = os.path.dirname(os.path.abspath(__file__))
    
    bat_path = os.path.join(script_dir, "Start_AutoReload.bat")
    
    # Launch the batch file hidden (no window)
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    
    subprocess.Popen(
        bat_path,
        cwd=script_dir,
        startupinfo=startupinfo,
        creationflags=subprocess.CREATE_NO_WINDOW
    )

if __name__ == "__main__":
    main()
