import os
import requests
import json
from Aawaz_utils import speak

def latestnews():
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        speak("Sir, News API key is missing.")
        return
    api_dict = {
        "business": f"https://newsapi.org/v2/top-headlines?category=business&apiKey={api_key}",
        "entertainment": f"https://newsapi.org/v2/top-headlines?category=entertainment&apiKey={api_key}",
        "health": f"https://newsapi.org/v2/top-headlines?category=health&apiKey={api_key}",
        "science": f"https://newsapi.org/v2/top-headlines?category=science&apiKey={api_key}",
        "sports": f"https://newsapi.org/v2/top-headlines?category=sports&apiKey={api_key}",
        "technology": f"https://newsapi.org/v2/top-headlines?category=technology&apiKey={api_key}"
    }

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")

