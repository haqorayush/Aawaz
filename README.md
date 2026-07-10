# 🎙️ Aawaz — AI Voice Agent System

> Aawaz is a modular, cross-platform **AI agent system with a voice interface** that can understand, reason, and act — combining LLM intelligence with real-world tool execution.

---

## 🚀 Overview

Aawaz started as a simple voice assistant and evolved into a **fully structured AI agent system**.

Unlike traditional assistants built on rigid rules, Aawaz uses:
- 🧠 **LLM-based reasoning**
- ⚙️ **Deterministic execution**
- 🔁 **Context-aware interactions**

This hybrid approach ensures both **flexibility (AI)** and **reliability (code)**.

---

## 🧠 Core Capabilities

### 🔹 AI Agent Intelligence
- LLM-powered intent reasoning (Groq + LLaMA 3)
- Structured JSON decision pipeline
- Parameter extraction from natural language
- Multi-step task execution
- Confidence scoring + clarification handling
- Context-aware conversation memory

### ⚙️ System Automation
- Application control (open/close apps)
- OS-level actions (shutdown, system control)
- Media & volume control
- Screenshot & system utilities

### 🌐 Real-Time Intelligence
- Weather reporting 🌤️  
- News aggregation 📰  
- IPL live scores 🏏  
- Wikipedia & web search 🔍  

### 🎤 Voice Interaction
- Speech-to-Text (STT)
- Text-to-Speech (TTS)
- Wake-word interaction
- Voice + text hybrid interface

### 🧘 Productivity Features
- Task scheduling
- Persistent memory (notes)
- Focus mode (website blocking + tracking)
- Usage visualization

---

## 🏗️ System Architecture

Voice Input / Text Input  
        ↓  
Speech-to-Text (STT)  
        ↓  
LLM Agent (Reasoning + Decision)  
        ↓  
Structured Output (JSON)  
        ↓  
Tool Execution Layer  
        ↓  
(Optional) LLM Response  
        ↓  
Text-to-Speech (TTS)  

---

## 🧩 Project Structure

```
aawaz/
│
├── main.py                 # Entry point
├── config.py               # Environment + config
│
├── audio/
│   ├── stt.py              # Speech-to-text
│   ├── tts.py              # Text-to-speech
│
├── core/
│   ├── assistant.py        # Central execution logic
│   ├── llm_agent.py        # LLM reasoning + decision system
│
├── features/
│   ├── search.py
│   ├── weather.py
│   ├── memory.py
│   ├── news.py
│   ├── ipl.py
│   ├── automation.py
│
├── system/
│   ├── os_controller.py    # Cross-platform OS handling
│
├── ui.py                   # Streamlit UI
```

---

## 🧠 AI Decision Pipeline

Example output from LLM agent:

```json
{
  "intent": "search",
  "platform": "youtube",
  "extracted_parameter": "relaxing music",
  "confidence": 0.92,
  "reason": "User wants to play relaxing music on YouTube"
}
```

---

## 🖥️ UI (Streamlit)

Aawaz includes a **real-time interactive UI**:

### Features:
- 💬 Chat interface (like ChatGPT)
- 🎤 Voice input support
- 🧠 AI Transparency Panel:
  - Intent
  - Extracted parameters
  - Confidence score
  - Selected tool
- 📊 Debug logs for system visibility
- ⚡ Quick action buttons (weather, news, etc.)

---

## ⚙️ Tech Stack

### Core
- Python 3.12

### AI / LLM
- Groq API (LLaMA 3 — 8B + 70B)

### Voice
- SpeechRecognition
- PyAudio
- pyttsx3 / gTTS

### Backend
- Requests
- BeautifulSoup
- WolframAlpha
- Wikipedia API

### UI
- Streamlit

---

## 🔐 Security

- API keys managed via `.env`
- No hardcoded credentials
- Config handled via `python-dotenv`

---

## 🛠️ Engineering Highlights

- Refactored monolithic script → modular architecture
- Designed hybrid LLM + deterministic system
- Implemented structured decision-making (JSON outputs)
- Built AI agent layer with reasoning + tool selection
- Added confidence-based fallback & clarification
- Introduced cross-platform OS abstraction (macOS + Windows)
- Integrated real-time UI with decision transparency
- Implemented error handling and execution safety

---

## 🎯 Why This Project Matters

Most assistants:  
> keyword → function  

Aawaz:  
> understand → reason → decide → execute  

This shift makes it closer to:
- **AI agents**
- **real-world automation systems**
- **next-gen human-computer interfaces**

---

## 📸 Demo

<img width="1710" height="985" alt="Screenshot 2026-05-05 at 12 37 23 PM" src="https://github.com/user-attachments/assets/87ef2b17-99e0-4f79-91ac-27dde64a6872" />


---

## ⚡ Getting Started

```bash
git clone https://github.com/haqorayush/Aawaz
cd Aawaz
pip install -r requirements.txt
streamlit run ui.py
```

---

## 🧪 Example Commands

- "Search YouTube and play something relaxing"
- "What's the weather in Delhi?"
- "Tell me the latest news"
- "Open Chrome"
- "Explain black holes"

---

## 📌 Future Improvements

- Full function-calling schema (OpenAI-style tools)
- Local LLM support (Ollama)
- Web deployment (public demo)
- Mobile integration
- Advanced memory system (long-term context)

---

> Built with the goal of moving from “scripts” to **real AI systems** 🚀
