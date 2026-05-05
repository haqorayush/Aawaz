import os
import json
from groq import Groq
from ..config import GROQ_API_KEY

if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)
else:
    client = None

INTENTS = [
    "system_control", "search", "productivity", "media", "general"
]

def llm_decide(query):
    if not client:
        return {"tool": "general_response", "arguments": {"query": query}, "reason": "No Groq API key", "confidence": "high", "clarification_question": ""}

    prompt = f"""
You are an AI assistant orchestrating a function-calling system.

Available tools:
1. system_control:
   - sleep() : put assistant to sleep
   - open_app(app_name: string) : launch applications or websites
   - close_app(app_name: string) : close applications or tabs
   - check_internet_speed() : check upload/download speed
   - take_screenshot() : take screen capture
   - click_photo() : take webcam photo
   - media_control(action: string) : play, pause, or mute media
   - volume_up() : increase volume
   - volume_down() : decrease volume
   - shutdown() : shutdown computer

2. search:
   - search_google(query: string) : search google
   - search_youtube(query: string) : use this WHENEVER the user asks to play any kind of music, song, artist, or video
   - search_wikipedia(query: string) : search wikipedia
   - get_news(category: string) : read top news headlines
   - get_weather(location: string) : check weather (pass "current" if location is not specified)
   - get_ipl_score() : check live cricket score

3. productivity & automation:
   - schedule_day(tasks: string) : schedule tasks
   - show_schedule() : view scheduled tasks
   - focus_mode() : enter distraction free mode
   - show_focus() : view focus graph
   - translate(query: string) : translate text
   - calculate(query: string) : math and wolfram alpha calculations
   - whatsapp(number: string, message: string) : send whatsapp message
   - set_alarm(time: string) : set an alarm in HH:MM:SS format
   - set_timer(seconds: int) : set a countdown timer for X seconds
   - start_stopwatch() : start a stopwatch
   - stop_stopwatch() : stop the stopwatch and report the time
   - get_time() : get current time
   - remember(text: string) : save text to memory
   - recall() : read saved memory

4. media:
   - play_game() : play a game
   - play_tired_music() : play general relaxing music
   - media_control(action: string) : resume, pause, or mute ALREADY running media (do NOT use this to play a new song)

5. general:
   - general_response(query: string) : general conversation, greetings, and unmapped questions

User query: "{query}"

Think step-by-step:
1. What does the user want?
2. Which tool matches this best?
3. What arguments does the tool need based on the query?
4. Calculate a numeric confidence score between 0.0 and 1.0.
5. If confidence is below 0.6, create a clarification_question. Otherwise leave empty.

Respond ONLY in valid JSON format:
{{
    "tool": "exact_tool_name_here",
    "arguments": {{
        "arg_name": "extracted_value"
    }},
    "reason": "your reasoning",
    "confidence": 0.95,
    "clarification_question": "question or empty string"
}}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            response_format={"type": "json_object"}
        )
        content = response.choices[0].message.content.strip()
        # Clean up potential markdown formatting that breaks json.loads
        if "```" in content:
            parts = content.split("```")
            content = parts[1] if len(parts) > 1 else content
            if content.startswith("json"):
                content = content[4:]
            content = content.strip()
            
        data = json.loads(content)
        tool = data.get("tool", "general_response").strip().lower()
        args = data.get("arguments", {})
        reason = data.get("reason", "")
        confidence = float(data.get("confidence", 1.0))
        clarification = data.get("clarification_question", "")
        
        print(f"\n[Agent Reasoning] {reason}")
        print(f"[Agent Tool] {tool} {args} (Confidence: {confidence})\n")
            
        return {
            "tool": tool, 
            "arguments": args,
            "reason": reason, 
            "confidence": confidence, 
            "clarification_question": clarification
        }
    except Exception as e:
        print(f"LLM Routing Error: {e}")
        return {"tool": "general_response", "arguments": {"query": query}, "reason": "Error parsing LLM response", "confidence": 1.0, "clarification_question": ""}

conversation_history = [
    {"role": "system", "content": "You are Aawaz, a highly intelligent and helpful AI voice assistant. Always keep your answers extremely concise and conversational, suitable for text-to-speech reading. Do not use markdown formatting like bolding or bullet points."}
]

def general_response(query):
    global conversation_history
    if not client:
        return "Sir, my Groq API key is missing. I cannot process general requests right now."

    conversation_history.append({"role": "user", "content": query})

    # Prevent infinite growth: Keep the system prompt + last 10 messages
    if len(conversation_history) > 11:
        conversation_history = [conversation_history[0]] + conversation_history[-10:]

    try:
        response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=conversation_history
        )

        reply = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": reply})

        return reply
    except Exception as e:
        print(f"LLM Response Error: {e}")
        return "I am having trouble connecting to my brain right now, sir."
