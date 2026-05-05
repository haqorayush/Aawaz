import os
import wolframalpha
from Jarvis_utils import speak

def WolfRamAlpha(query):
    apikey = os.getenv("WOLFRAMALPHA_APP_ID")
    if not apikey:
        speak("Sir, WolframAlpha API key is missing.")
        return None
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")

        