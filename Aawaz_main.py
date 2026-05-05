import datetime
import webbrowser
import requests
from bs4 import BeautifulSoup
import os
import subprocess
import sys
import pyautogui
import random
from plyer import notification
from pygame import mixer
import speedtest 

# Local imports
from Aawaz_utils import speak, takeCommand
from GreetMe import greetMe
from FocusGraph import focus_graph
from Translator import translategl
from Dictapp import openappweb, closeappweb
from game import game_play
from keyboard import volumeup, volumedown
from SearchNow import searchGoogle, searchYoutube, searchWikipedia
from NewsRead import latestnews
from Calculatenumbers import WolfRamAlpha, Calc
from Whatsapp import sendMessage

print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    subprocess.Popen([sys.executable, "alarm.py"])



if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 
                
                #################### AAWAZ: THe Trilogy 2.0 #####################

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write("")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    try:
                        with open("tasks.txt", "r") as file:
                            content = file.read()
                        if not content.strip():
                            content = "You have no tasks scheduled."
                        mixer.init()
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

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        subprocess.Popen([sys.executable, "FocusMode.py"])
                        exit()

                    
                    else:
                        pass

                elif "show my focus" in query:
                    focus_graph()

                elif "translate" in query:
                    query = query.replace("aawaz","")
                    query = query.replace("translate","")
                    translategl(query)

                elif "open" in query:
                    openappweb(query)

                elif "close" in query:
                    closeappweb(query)
                     
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                    

                elif "ipl score" in query:
                    try:
                        url = "https://www.cricbuzz.com/"
                        page = requests.get(url, timeout=10)
                        soup = BeautifulSoup(page.text,"html.parser")
                        teams = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")
                        if len(teams) >= 2:
                            team1 = teams[0].get_text()
                            team2 = teams[1].get_text()
                            scores = soup.find_all(class_ = "cb-ovr-flo")
                            # Note: indices might still be fragile but try/except handles it
                            team1_score = scores[8].get_text() if len(scores) > 8 else "N/A"
                            team2_score = scores[10].get_text() if len(scores) > 10 else "N/A"

                            print(f"{team1} : {team1_score}")
                            print(f"{team2} : {team2_score}")

                            notification.notify(
                                title = "IPL SCORE :- ",
                                message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                                timeout = 15
                            )
                        else:
                            speak("I couldn't find any live IPL scores right now.")
                    except Exception as e:
                        print(f"IPL scraping error: {e}")
                        speak("Sorry sir, I had trouble getting the IPL scores.")

                
                elif "play a game" in query:
                    game_play()

                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                

                ############################################################
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://youtu.be/76xYGwiFEGQ")
                    elif b==2:
                        webbrowser.open("https://youtu.be/76xYGwiFEGQ")
                    elif b==3:
                        webbrowser.open("https://youtu.be/76xYGwiFEGQ")
                    

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                


                elif "volume up" in query:
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    speak("Turning volume down, sir")
                    volumedown()


                elif "google" in query:
                    searchGoogle(query)
                elif "youtube" in query:
                    searchYoutube(query)
                elif "wikipedia" in query:
                    searchWikipedia(query)

                
                elif "news" in query:
                    latestnews()

                elif "calculate" in query:
                    query = query.replace("calculate","")
                    query = query.replace("aawaz","")
                    Calc(query)

                elif "whatsapp" in query:
                    sendMessage()

                

                elif "temperature" in query or "weather" in query:
                    # Extract city from query, default to "delhi"
                    city = query.replace("aawaz","").replace("temperature","").replace("weather","")
                    city = city.replace("what is the","").replace("today","").replace("in","").replace("of","").strip()
                    if not city:
                        city = "delhi"
                    try:
                        url = f"https://wttr.in/{city}?format=%l:+%C+%t+%h+%w"
                        r = requests.get(url, timeout=10)
                        if r.status_code == 200 and "Unknown" not in r.text:
                            weather_info = r.text.strip()
                            print(f"Weather: {weather_info}")
                            speak(f"The current weather in {city} is {weather_info}")
                        else:
                            speak(f"Sorry sir, I could not find the weather for {city}")
                    except Exception as e:
                        print(f"Weather error: {e}")
                        speak("Sorry sir, I could not fetch the weather right now")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                           
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = rememberMessage.replace("aawaz","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    try:
                        with open("Remember.txt", "r") as file:
                            content = file.read()
                        if content.strip():
                            speak("You told me to remember that " + content)
                        else:
                            speak("I don't have anything in my memory right now.")
                    except FileNotFoundError:
                        speak("I don't remember anything yet, sir.")

                elif "shutdown system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        if sys.platform == "darwin":
                            os.system("osascript -e 'tell app \"System Events\" to shut down'")
                        else:
                            os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break