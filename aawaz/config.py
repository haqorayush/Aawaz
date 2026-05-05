import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WOLFRAMALPHA_APP_ID = os.getenv("WOLFRAMALPHA_APP_ID")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
