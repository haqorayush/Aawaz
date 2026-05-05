import webbrowser
import pywhatkit
import wikipedia
import wolframalpha
from deep_translator import GoogleTranslator
from ..audio.tts import speak
from ..config import WOLFRAMALPHA_APP_ID

def searchGoogle(query):
    import wikipedia as googleScrap
    query = query.replace("aawaz","").replace("google search","").replace("google","").strip()
    if not query:
        speak("What should I search for on Google?")
        return
    speak(f"Searching Google for {query}")
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,1)
        speak(result)
    except:
        speak("I opened Google for you.")

def searchYoutube(query):
    query = query.replace("youtube search","").replace("youtube","").replace("aawaz","").strip()
    if not query:
        speak("What should I search for on YouTube?")
        return
    speak(f"Playing {query} on YouTube")
    pywhatkit.playonyt(query)

def searchWikipedia(query):
    query = query.replace("wikipedia","").replace("search wikipedia","").replace("aawaz","").strip()
    if not query:
        speak("What should I search for on Wikipedia?")
        return
    
    speak(f"Searching Wikipedia for {query}")
    try:
        # Search for the best match first
        search_results = wikipedia.search(query)
        if not search_results:
            speak(f"I couldn't find any Wikipedia pages for {query}")
            return
            
        # Fetch summary for the top result
        # auto_suggest=False prevents it from changing "Donald J Trump" to something else wrongly
        Results = wikipedia.summary(search_results[0], sentences=2, auto_suggest=False)
        print(Results)
        speak(f"According to Wikipedia: {Results}")
    except wikipedia.exceptions.DisambiguationError as e:
        # Pick the first option if it's a disambiguation page
        try:
            Results = wikipedia.summary(e.options[0], sentences=2, auto_suggest=False)
            speak(f"According to Wikipedia: {Results}")
        except:
            speak("I found multiple results for that, sir. Could you be more specific?")
    except Exception as e:
        print(f"Wikipedia Error: {e}")
        speak("I could not find a summary for that on Wikipedia.")

def translategl(query):
    speak("SURE SIR")
    try:
        text = GoogleTranslator(source='auto', target='hi').translate(query)
        print(f"Translated: {text}")
        speak("Here is the translation")
        from gtts import gTTS
        import os
        from playsound import playsound
        speakgtts = gTTS(text=text, lang="hi", slow=False)
        speakgtts.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
    except Exception as e:
        print(f"Translation Error: {e}")
        speak("Sorry sir, I could not translate that.")

def calc(query):
    # Standardize math operators for both local eval and WolframAlpha
    term = str(query).lower().replace("aawaz","")
    term = term.replace("multiply", "*").replace("times", "*").replace("x", "*")
    term = term.replace("plus", "+").replace("minus", "-").replace("divide", "/").replace("by", "/")
    term = term.strip()
    
    # Try local evaluation for simple arithmetic (fast & works offline)
    try:
        # Only allow numbers and basic math operators for safety
        safe_chars = "0123456789+-*/(). "
        if term and all(c in safe_chars for c in term):
            # Evaluate the math expression
            result = eval(term)
            print(f"Local Math Result: {result}")
            speak(f"The answer is {result}")
            return
    except Exception as e:
        print(f"Local Math Error: {e}")
        pass

    # Fallback to WolframAlpha for complex knowledge queries
    if not WOLFRAMALPHA_APP_ID:
        speak("I couldn't calculate that locally, and the WolframAlpha API key is missing.")
        return
        
    try:
        requester = wolframalpha.Client(WOLFRAMALPHA_APP_ID)
        requested = requester.query(term)
        answer = next(requested.results).text
        print(f"WolframAlpha Result: {answer}")
        speak(answer)
    except:
        speak("The value is not answerable, sir.")
