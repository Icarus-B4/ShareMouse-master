import subprocess
import time
import os

# Configuration
POSSIBLE_PATHS = [
    r"C:\Program Files (x86)\ShareMouse\ShareMouse.exe",
    r"C:\Program Files\ShareMouse\ShareMouse.exe"
]
INTERVAL_SECONDS = 300  # 5 minutes

def get_sharemouse_path():
    """Finds the ShareMouse executable in common locations."""
    for path in POSSIBLE_PATHS:
        if os.path.exists(path):
            return path
    return None

SHAREMOUSE_PATH = get_sharemouse_path()

def stop_sharemouse():
    """Stops the ShareMouse process if it's running."""
    print("Stopping ShareMouse...")
    # /F forces termination, /IM specifies image name
    subprocess.call("taskkill /F /IM ShareMouse.exe", shell=True)

def start_sharemouse():
    """Starts the ShareMouse process."""
    if SHAREMOUSE_PATH and os.path.exists(SHAREMOUSE_PATH):
        print(f"Starting ShareMouse from {SHAREMOUSE_PATH}...")
        subprocess.Popen(SHAREMOUSE_PATH)
    else:
        print(f"Error: ShareMouse not found in common locations.")
        print(f"Checked: {POSSIBLE_PATHS}")

def main():
    print("ShareMouse Auto-Reload for Windows started.")
    print(f"Interval: {INTERVAL_SECONDS} seconds")
    print("Press Ctrl+C to exit.")

    try:
        while True:
            stop_sharemouse()
            time.sleep(2) # Give it a moment to close completely
            start_sharemouse()
            
            print(f"Waiting {INTERVAL_SECONDS} seconds...")
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nScript stopped by user.")

if __name__ == "__main__":
    main()
