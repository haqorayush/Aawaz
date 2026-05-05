import subprocess
import sys
import random
import webbrowser
from datetime import datetime, timedelta
import pywhatkit
from ..audio.tts import speak

import os
import threading
import time

STOPWATCH_FILE = ".stopwatch_state"

stopwatch_start = None

def set_alarm(time_str):
    if not time_str:
        speak("Please provide a valid time for the alarm.")
        return
    # Ensure HH:MM:SS format
    if len(time_str.split(":")) == 2:
        time_str += ":00"
    
    with open("Alarmtext.txt", "w") as timehere:
        timehere.write(time_str)
    subprocess.Popen([sys.executable, "alarm.py"])
    speak(f"Alarm set for {time_str}.")

def set_timer(seconds):
    speak(f"Timer set for {seconds} seconds.")
    def timer_callback():
        speak("Time's up! Your timer has finished.")
        # Play a sound if possible
        if sys.platform == "darwin":
            os.system("afplay /System/Library/Sounds/Glass.aiff")
    
    threading.Timer(seconds, timer_callback).start()

def start_stopwatch():
    start_time = time.time()
    with open(STOPWATCH_FILE, "w") as f:
        f.write(str(start_time))
    speak("Stopwatch started.")

def stop_stopwatch():
    if not os.path.exists(STOPWATCH_FILE):
        speak("The stopwatch wasn't running, sir.")
    else:
        with open(STOPWATCH_FILE, "r") as f:
            start_time = float(f.read())
        os.remove(STOPWATCH_FILE)
        elapsed = time.time() - start_time
        minutes, seconds = divmod(elapsed, 60)
        speak(f"Stopwatch stopped. Elapsed time: {int(minutes)} minutes and {int(seconds)} seconds.")

def start_focus_mode():
# ... (existing code)
    speak("Entering the focus mode....")
    subprocess.Popen([sys.executable, "FocusMode.py"])

def show_focus_graph():
    from FocusGraph import focus_graph
    focus_graph()

def play_game():
    from game import game_play
    game_play()

def send_whatsapp(number, message):
    if not number or not message:
        speak("Please provide both a number and a message.")
        return
    strTime = int(datetime.now().strftime("%H"))
    update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))
    try:
        pywhatkit.sendwhatmsg(number, message, strTime, update)
        speak("Message scheduled successfully.")
    except Exception as e:
        speak("Failed to send WhatsApp message.")

def play_tired_music():
    speak("Playing your favourite songs, sir")
    a = (1,2,3)
    b = random.choice(a)
    if b==1:
        webbrowser.open("https://youtu.be/76xYGwiFEGQ")
    elif b==2:
        webbrowser.open("https://youtu.be/76xYGwiFEGQ")
    elif b==3:
        webbrowser.open("https://youtu.be/76xYGwiFEGQ")

