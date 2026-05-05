import requests
from bs4 import BeautifulSoup
from plyer import notification
from ..audio.tts import speak

def ipl_score():
    try:
        url = "https://www.cricbuzz.com/"
        page = requests.get(url, timeout=10)
        soup = BeautifulSoup(page.text,"html.parser")
        
        # Find the first live match block
        match_block = soup.find(class_="cb-mtch-crd-rt-clm")
        if match_block:
            teams = match_block.find_all(class_="cb-hmscg-tm-nm")
            scores = match_block.find_all(class_="cb-ovr-flo")
            
            if len(teams) >= 2:
                team1 = teams[0].get_text()
                team2 = teams[1].get_text()
                
                # Get text for scores if available
                team1_score = scores[0].get_text() if len(scores) > 0 else "N/A"
                team2_score = scores[1].get_text() if len(scores) > 1 else "N/A"

                print(f"{team1} : {team1_score}")
                print(f"{team2} : {team2_score}")

                notification.notify(
                    title = "IPL SCORE :- ",
                    message = f"{team1} : {team1_score}\n{team2} : {team2_score}",
                    timeout = 15
                )
                speak(f"The score is {team1} {team1_score} and {team2} {team2_score}")
                return
                
        speak("I couldn't find any live cricket match scores right now.")
    except Exception as e:
        print(f"IPL scraping error: {e}")
        speak("Sorry sir, I had trouble getting the cricket scores.")
