import sys
import subprocess
import pyttsx3

spoken_history = []

def clear_spoken_history():
    global spoken_history
    spoken_history = []

def get_spoken_history():
    global spoken_history
    return spoken_history

def get_engine():
    if sys.platform == "darwin":
        return None
    elif sys.platform == "win32":
        return pyttsx3.init("sapi5")
    else:
        return pyttsx3.init()

def speak(audio):
    global spoken_history
    spoken_history.append(str(audio))
    print(f"AAWAZ: {audio}")
    if sys.platform == "darwin":
        MACOS_VOICE = "Daniel" 
        subprocess.run(["say", "-v", MACOS_VOICE, "-r", "180", str(audio)])
    else:
        engine = get_engine()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        engine.setProperty("rate", 170)
        engine.say(audio)
        engine.runAndWait()
