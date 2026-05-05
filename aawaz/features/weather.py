import requests
from ..audio.tts import speak

def get_current_city():
    try:
        # Use ip-api.com to get city from IP address
        response = requests.get("http://ip-api.com/json/", timeout=5)
        data = response.json()
        return data.get("city", "delhi")
    except:
        return "delhi"

def get_weather(query):
    # Clean query to check if a specific city was mentioned
    city = query.replace("aawaz","").replace("temperature","").replace("weather","")
    city = city.replace("what is the","").replace("today","").replace("in","").replace("of","").replace("my","").strip()
    
    # If no city extracted, or query is a generic "weather" request, fetch current location
    if not city or city.lower() in ["current", "here", "location"]:
        city = get_current_city()
        speak(f"Checking the weather for your current location, {city}.")
    
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
