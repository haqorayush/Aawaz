import pywhatkit
from datetime import datetime, timedelta
from Jarvis_utils import speak

def sendMessage():
    strTime = int(datetime.now().strftime("%H"))
    update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

    speak("Who do you wan to message")
    a = int(input('''Person 1 - 1
    Person 2 - 2'''))
    if a == 1:
        speak("Whats the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+91000000000",message,time_hour=strTime,time_min=update) #Enter The number here instead of +91000
    elif a==2:
        pass

