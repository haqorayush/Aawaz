import os
from plyer import notification
from pygame import mixer
from ..audio.tts import speak
from ..audio.stt import listen

def schedule_day(query):
    tasks = []
    speak("Do you want to clear old tasks (Plz speak YES or NO)")
    confirmation = listen().lower()
    if "yes" in confirmation:
        with open("tasks.txt","w") as file:
            file.write("")
        no_tasks = int(input("Enter the no. of tasks :- "))
        for i in range(no_tasks):
            tasks.append(input("Enter the task :- "))
            with open("tasks.txt","a") as file:
                file.write(f"{i}. {tasks[i]}\n")
    elif "no" in confirmation:
        no_tasks = int(input("Enter the no. of tasks :- "))
        for i in range(no_tasks):
            tasks.append(input("Enter the task :- "))
            with open("tasks.txt","a") as file:
                file.write(f"{i}. {tasks[i]}\n")

def show_schedule():
    try:
        with open("tasks.txt", "r") as file:
            content = file.read()
        if not content.strip():
            content = "You have no tasks scheduled."
        mixer.init()
        # Ensure notification.mp3 exists or catch error
        if os.path.exists("notification.mp3"):
            mixer.music.load("notification.mp3")
            mixer.music.play()
        notification.notify(
            title = "My schedule :-",
            message = content,
            timeout = 15
        )
    except FileNotFoundError:
        speak("Sir, you haven't created a schedule yet.")
    except Exception as e:
        speak("Sorry sir, I couldn't read your schedule.")

def remember_that(query):
    rememberMessage = query.replace("remember that","").replace("aawaz","")
    speak("You told me to remember that" + rememberMessage)
    with open("Remember.txt","a") as remember:
        remember.write(rememberMessage)

def what_do_you_remember():
    try:
        with open("Remember.txt", "r") as file:
            content = file.read()
        if content.strip():
            speak("You told me to remember that " + content)
        else:
            speak("I don't have anything in my memory right now.")
    except FileNotFoundError:
        speak("I don't remember anything yet, sir.")
