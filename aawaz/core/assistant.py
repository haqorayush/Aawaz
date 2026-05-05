from ..audio.stt import listen
from ..audio.tts import speak, clear_spoken_history, get_spoken_history
from .llm_agent import llm_decide, general_response
import datetime

# Feature imports
from ..features.search import searchGoogle, searchYoutube, searchWikipedia, translategl, calc
from ..features.weather import get_weather
from ..features.memory import schedule_day, show_schedule, remember_that, what_do_you_remember
from ..features.automation import set_alarm, start_focus_mode, show_focus_graph, play_game, send_whatsapp, play_tired_music, set_timer, start_stopwatch, stop_stopwatch
from ..features.news import latest_news
from ..features.ipl import ipl_score
from ..system.os_controller import openappweb, closeappweb, volumeup, volumedown, shutdown_system, take_screenshot, click_photo, check_internet_speed, media_control

last_query = None
last_decision = {}

def handle_query(query):
    global last_query
    global last_decision
    
    clear_spoken_history()
    
    if "again" in query and last_query:
        query = last_query
        speak(f"Repeating: {query}")
        
    decision = llm_decide(query)
    last_decision = decision
    tool = decision.get("tool", "general_response")
    args = decision.get("arguments", {})
    
    # Handle low confidence gracefully
    if decision.get("confidence", 1.0) < 0.6 and decision.get("clarification_question"):
        speak(decision["clarification_question"])
        return True
        
    # Execute the requested tool
    try:
        if tool == "sleep":
            speak("Ok sir , You can call me anytime")
            return False
        elif tool == "open_app": openappweb(args.get("app_name", ""))
        elif tool == "close_app": closeappweb(args.get("app_name", ""))
        elif tool == "check_internet_speed": check_internet_speed()
        elif tool == "take_screenshot": take_screenshot()
        elif tool == "click_photo": click_photo()
        elif tool == "media_control": media_control(args.get("action", ""))
        elif tool == "volume_up": volumeup()
        elif tool == "volume_down": volumedown()
        elif tool == "shutdown": shutdown_system()
        
        elif tool == "search_google": searchGoogle(args.get("query", ""))
        elif tool == "search_youtube": searchYoutube(args.get("query", ""))
        elif tool == "search_wikipedia": searchWikipedia(args.get("query", ""))
        elif tool == "get_news": latest_news(args.get("category", "general"))
        elif tool == "get_weather": get_weather(args.get("location", query))
        elif tool == "get_ipl_score": ipl_score()
        
        elif tool == "schedule_day": schedule_day(args.get("tasks", ""))
        elif tool == "show_schedule": show_schedule()
        elif tool == "focus_mode": start_focus_mode()
        elif tool == "show_focus": show_focus_graph()
        elif tool == "translate": translategl(args.get("query", ""))
        elif tool == "calculate": calc(args.get("query", ""))
        elif tool == "whatsapp": send_whatsapp(args.get("number", ""), args.get("message", ""))
        elif tool == "set_alarm": set_alarm(args.get("time", ""))
        elif tool == "set_timer": set_timer(args.get("seconds", 0))
        elif tool == "start_stopwatch": start_stopwatch()
        elif tool == "stop_stopwatch": stop_stopwatch()
        elif tool == "get_time":
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")
        elif tool == "remember": remember_that(args.get("text", ""))
        elif tool == "recall": what_do_you_remember()
        
        elif tool == "play_game": play_game()
        elif tool == "play_tired_music": play_tired_music()
        
        elif tool == "general_response":
            # Check standard conversational fast-paths first
            if "hello" in query: speak("Hello sir, how are you ?")
            elif "i am fine" in query: speak("that's great, sir")
            elif "how are you" in query: speak("Perfect, sir")
            elif "thank you" in query: speak("you are welcome, sir")
            else:
                speak(general_response(args.get("query", query)))
        else:
            speak(general_response(query))
            
    except Exception as e:
        print(f"Execution Error: {e}")
        speak("I encountered an error while trying to do that. Please try again.")
            
    history = get_spoken_history()
    final_response = "\n\n".join(history) if history else "Command executed successfully (Audio output played)."
    
    if tool == "sleep":
        final_response = "Assistant entering sleep mode."
        
    return {
        "response": final_response,
        "intent": decision.get("reason", ""),
        "parameter": str(args),
        "confidence": decision.get("confidence", 1.0),
        "tool": tool
    }

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning, sir")
    elif hour > 12 and hour <= 18:
        speak("Good Afternoon, sir")
    else:
        speak("Good Evening, sir")
    speak("Please tell me, How can I help you ?")


