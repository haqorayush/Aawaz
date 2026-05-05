import requests
from ..audio.tts import speak
from ..config import NEWS_API_KEY

def latest_news(category="general"):
    if not NEWS_API_KEY:
        speak("Sir, News API key is missing.")
        return
    
    url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={NEWS_API_KEY}"
    if category.lower() not in ["business", "entertainment", "health", "science", "sports", "technology", "general"]:
        url = f"https://newsapi.org/v2/top-headlines?category=general&apiKey={NEWS_API_KEY}"

    try:
        news = requests.get(url).json()
        speak(f"Here are the top {category} news headlines.")
        arts = news.get("articles", [])[:3]
        for article in arts:
            title = article["title"]
            print(title)
            speak(title)
        speak("That's all for the top news.")
    except Exception as e:
        speak("Could not fetch news.")
