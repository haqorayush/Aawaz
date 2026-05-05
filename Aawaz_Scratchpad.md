# 🎙️ Aawaz - Scratchpad

## 1. Project Name
**Aawaz** (An advanced Python-based Desktop Voice Assistant)

## 2. Tech Stack
*   **Core**: Python 3.12+
*   **Speech Recognition**: `SpeechRecognition` (using Google Web Speech API)
*   **Text-to-Speech (TTS)**: 
    *   **macOS**: Native `say` command (high-quality British/Indian English voices)
    *   **Windows**: `pyttsx3` with `sapi5` engine
*   **Automation & Web**: `pywhatkit`, `webbrowser`, `pyautogui`, `requests`, `BeautifulSoup` (Scraping)
*   **Knowledge & APIs**: `wolframalpha` (Math/Science), `wikipedia`, `wttr.in` (Weather), `NewsAPI`
*   **Multimedia & UI**: `pygame` (Audio playback), `plyer` (Desktop notifications), `matplotlib` (Data visualization)
*   **Environment Management**: `python-dotenv` (Secure API key handling)

## 3. Compatibility
*   ✅ **macOS**: Fully optimized for Apple Silicon and Intel (tested on macOS Sonoma/Sequoia).
*   ✅ **Windows**: Supports Windows 10/11 with native SAPI5 voices.
*   ✅ **Cross-Platform**: Unified codebase using platform-aware logic.

## 4. Features
*   **Voice Activation**: "Wake up" activation and "Go to sleep" standby mode.
*   **Smart Search**: Intelligent routing between Google, YouTube, and Wikipedia.
*   **System Mastery**:
    *   Open/Close applications (Chrome, VS Code, Terminal, etc.).
    *   Media control (Play, Pause, Mute, Volume Up/Down).
    *   System controls (Screenshot, Photo capture, Shutdown).
*   **Information Hub**:
    *   Real-time weather (via wttr.in).
    *   Live IPL scores and news headlines.
    *   Complex calculations and scientific queries (WolframAlpha).
*   **Productivity**:
    *   Daily task scheduling ("Schedule my day").
    *   Persistent memory ("Remember that...").
    *   Focus Mode (Website blocking and usage graphing).
*   **Entertainment**: Rock-Paper-Scissors game and randomized favorite music playback.

## 5. Use Case Examples
*   **The Student**: "Jarvis, calculate the derivative of x squared" or "Search Wikipedia for Quantum Physics."
*   **The Power User**: "Jarvis, open VS Code" or "Jarvis, what is my internet speed?"
*   **Daily Routine**: "Jarvis, what is the weather in Mumbai?" followed by "Jarvis, read the news."
*   **Memory Aid**: "Jarvis, remember that my keys are in the second drawer." Later: "Jarvis, what do you remember?"

## 6. Future Roadmap
*   **GUI Integration**: Transition from terminal-based to a sleek, glassmorphic desktop interface.
*   **LLM Power-up**: Integrate Google Gemini or OpenAI GPT for natural, multi-turn conversations.
*   **IoT Integration**: Control smart home devices (Lights, Fans) via Home Assistant API.
*   **Custom Voice Models**: Support for local, high-fidelity TTS models (like ElevenLabs or Coqui TTS).
*   **Mobile Sync**: A companion mobile app to view schedules and "Remember" notes on the go.
