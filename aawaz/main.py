import sys
import os

# Add project root to path so we can import absolute if needed
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aawaz.audio.stt import listen
from aawaz.core.assistant import handle_query, greetMe

def main():
    print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
    while True:
        query = listen()
        if not query or query.lower() == "none":
            continue
        query = query.lower()
        
        if "wake up" in query:
            greetMe()
            while True:
                query = listen()
                if not query or query.lower() == "none":
                    continue
                query = query.lower()
                
                should_continue = handle_query(query)
                if not should_continue:
                    break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting Aawaz. Goodbye!")
        sys.exit(0)
