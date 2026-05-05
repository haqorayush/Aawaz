# AAWAZ - Desktop Voice Assistant

A Python-based desktop assistant inspired by Iron Man's JARVIS. This project handles voice commands for various tasks like web searches, system control, scheduling, and more.

## Formal Project Summary

[**Pre-Audit Report**](https://drive.google.com/file/d/1EqSjwomw2K0cwBBxW_xQIHzjaldWQpeE/view?usp=sharing) / [**Final Report**](https://drive.google.com/file/d/1UAc9UyIgyeARoYDOKDFNNbqF-cGG8QXy/view?usp=share_link) / [**Audio Report**](https://drive.google.com/file/d/1a79y6Da4uIZN8yGpfmdE6yR1jOpyUqM1/view?usp=sharing) / [**Final Presentation**](https://drive.google.com/file/d/1XiP7soMKq_UnIOvbfozp7nxGq3CXlD47/view?usp=sharing)

## Features

Aawaz comes packed with a variety of useful features:

- **Voice Control**: Activated by saying "Wake up".
- **Cross-Platform**: Supports Windows and macOS (high-quality native voice on Mac).
- **Web Tasks**: Google search, YouTube playback, Wikipedia summaries.
- **System Control**: Open/Close apps, volume control, screenshots, and shutdown.
- **Productivity**: Daily task scheduling, "Remember" notes, Focus mode.
- **Entertainment**: IPL scores, favorite music, and Rock-Paper-Scissors.

## Setup Instructions

### 1. Requirements
Ensure you have Python 3.12+ installed.

### 2. Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Dependencies
On macOS, you may need to install `portaudio` for microphone access:
```bash
brew install portaudio
```

### 4. API Keys
This project uses environment variables to manage API keys safely.
1.  Copy the `.env.example` file and rename it to `.env`.
2.  Add your keys inside the `.env` file:
    *   `NEWS_API_KEY`: Get from [NewsAPI.org](https://newsapi.org/).
    *   `WOLFRAMALPHA_APP_ID`: Get from [WolframAlpha Developer Portal](https://developer.wolframalpha.com/).

## Usage
Run the main script:
```bash
python Jarvis_main.py
```
Speak **"Wake up"** to start the assistant, and **"Go to sleep"** to put it on standby.

## Future Hosting Plans
This project is designed to be shared and hosted on platforms like GitHub. Ensure you keep your API keys private!

## 🤝 Contributing
Contributions are welcome! If you'd like to improve Aawaz:

- Fork the repository.
- Create a new branch (git checkout -b feature/YourFeature).
- Commit your changes.
- Push to the branch.
- Open a Pull Request.

## License
This project is open-source. Please check the repository for specific license information.

