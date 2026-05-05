import os 
import pyautogui
import webbrowser
import sys
from time import sleep
from Jarvis_utils import speak

# Dictionary mapping common names to executable names
# For macOS, these should match application names in /Applications
dictapp = {
    "commandprompt": "Terminal" if sys.platform == "darwin" else "cmd",
    "paint": "Photos" if sys.platform == "darwin" else "mspaint", # No direct paint on Mac
    "word": "Microsoft Word" if sys.platform == "darwin" else "winword",
    "excel": "Microsoft Excel" if sys.platform == "darwin" else "excel",
    "chrome": "Google Chrome" if sys.platform == "darwin" else "chrome",
    "vscode": "Visual Studio Code" if sys.platform == "darwin" else "code",
    "powerpoint": "Microsoft PowerPoint" if sys.platform == "darwin" else "powerpnt"
}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                if sys.platform == "darwin":
                    os.system(f"open -a '{dictapp[app]}'")
                else:
                    os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing,sir")
    # Hotkey for closing tabs: Cmd+W on Mac, Ctrl+W on others
    modifier = "command" if sys.platform == "darwin" else "ctrl"
    
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey(modifier, "w")
        speak("Tab closed")
    elif "2 tab" in query:
        pyautogui.hotkey(modifier, "w")
        sleep(0.5)
        pyautogui.hotkey(modifier, "w")
        speak("Tabs closed")
    elif "3 tab" in query:
        for _ in range(3):
            pyautogui.hotkey(modifier, "w")
            sleep(0.5)
        speak("Tabs closed")
    # ... Simplified further for maintenance
    elif any(f"{i} tab" in query for i in range(4, 10)):
        num = next(int(s) for s in query.split() if s.isdigit())
        for _ in range(num):
            pyautogui.hotkey(modifier, "w")
            sleep(0.5)
        speak(f"{num} tabs closed")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                if sys.platform == "darwin":
                    # pkill is often safer than killall for fuzzy matching
                    os.system(f"pkill -x '{dictapp[app]}'")
                else:
                    os.system(f"taskkill /f /im {dictapp[app]}.exe")