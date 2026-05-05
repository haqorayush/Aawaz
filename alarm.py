import pyttsx3
import datetime
import os
import sys
import subprocess

# Auto-detect TTS driver based on OS
if sys.platform == "darwin":
    engine = pyttsx3.init("nsss")
elif sys.platform == "win32":
    engine = pyttsx3.init("sapi5")
else:
    engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow).strip()
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            # Cross-platform: open music file
            if sys.platform == "darwin":
                subprocess.Popen(["open", "music.mp3"])
            elif sys.platform == "win32":
                os.startfile("music.mp3")
            else:
                subprocess.Popen(["xdg-open", "music.mp3"])
            break

ring(Time)
