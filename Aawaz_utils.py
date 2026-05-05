import subprocess
import speech_recognition
import os
import sys
import pyttsx3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Auto-detect TTS based on OS
def get_engine():
    if sys.platform == "darwin":
        # We can use 'say' or 'nsss' driver for pyttsx3. 
        # Aawaz_main.py was using subprocess 'say' which sounds better on macOS.
        return None
    elif sys.platform == "win32":
        return pyttsx3.init("sapi5")
    else:
        return pyttsx3.init()

def speak(audio):
    print(f"AAWAZ: {audio}")
    if sys.platform == "darwin":
        # macOS: use the native 'say' command for high-quality voice
        MACOS_VOICE = "Daniel" 
        subprocess.run(["say", "-v", MACOS_VOICE, "-r", "180", str(audio)])
    else:
        engine = get_engine()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        engine.setProperty("rate", 170)
        engine.say(audio)
        engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, 0, 4)
        except Exception:
            return "None"

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
