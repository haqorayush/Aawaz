import os
import platform
import subprocess
import pyautogui
import speedtest
import webbrowser
from time import sleep
from pynput.keyboard import Key, Controller
from ..audio.tts import speak

keyboard = Controller()

# Dictionary mapping common names to executable names
dictapp = {
    "commandprompt": "Terminal" if platform.system() == "Darwin" else "cmd",
    "paint": "Photos" if platform.system() == "Darwin" else "mspaint",
    "word": "Microsoft Word" if platform.system() == "Darwin" else "winword",
    "excel": "Microsoft Excel" if platform.system() == "Darwin" else "excel",
    "chrome": "Google Chrome" if platform.system() == "Darwin" else "chrome",
    "vscode": "Visual Studio Code" if platform.system() == "Darwin" else "code",
    "powerpoint": "Microsoft PowerPoint" if platform.system() == "Darwin" else "powerpnt"
}

def open_app(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", "-a", path])

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("aawaz","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                open_app(dictapp[app])

def closeappweb(query):
    speak("Closing,sir")
    modifier = "command" if platform.system() == "Darwin" else "ctrl"
    
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey(modifier, "w")
        speak("Tab closed")
    elif "2 tab" in query:
        for _ in range(2):
            pyautogui.hotkey(modifier, "w")
            sleep(0.5)
        speak("Tabs closed")
    elif "3 tab" in query:
        for _ in range(3):
            pyautogui.hotkey(modifier, "w")
            sleep(0.5)
        speak("Tabs closed")
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
                if platform.system() == "Darwin":
                    subprocess.Popen(["pkill", "-x", dictapp[app]])
                else:
                    os.system(f"taskkill /f /im {dictapp[app]}.exe")

def volumeup():
    speak("Turning volume up,sir")
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def volumedown():
    speak("Turning volume down, sir")
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

def shutdown_system():
    speak("Are You sure you want to shutdown")
    shutdown = input("Do you wish to shutdown your computer? (yes/no): ")
    if shutdown.lower() == "yes":
        if platform.system() == "Windows":
            os.system("shutdown /s /t 1")
        elif platform.system() == "Darwin":
            os.system("osascript -e 'tell app \"System Events\" to shut down'")

def take_screenshot():
    im = pyautogui.screenshot()
    im.save("ss.jpg")

def click_photo():
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    pyautogui.sleep(2)
    speak("SMILE")
    pyautogui.press("enter")

def check_internet_speed():
    wifi  = speedtest.Speedtest()
    upload_net = wifi.upload()/1048576
    download_net = wifi.download()/1048576
    print("Wifi Upload Speed is", upload_net)
    print("Wifi download speed is ",download_net)
    speak(f"Wifi download speed is {download_net}")
    speak(f"Wifi Upload speed is {upload_net}")

def media_control(action):
    if action == "pause" or action == "play":
        pyautogui.press("k")
        speak(f"video {action}ed")
    elif action == "mute":
        pyautogui.press("m")
        speak("video muted")

