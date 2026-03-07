# Aawaz 🎙️

**Aawaz** is an AI-based personal voice assistant designed to help you automate tasks, retrieve information, and manage your daily routine using voice commands. It functions similarly to assistants like Jarvis, capable of performing web searches, playing music, reading news, and more.

## Formal Project Summary

[**Click Here to Read**](https://drive.google.com/file/d/1UAc9UyIgyeARoYDOKDFNNbqF-cGG8QXy/view?usp=share_link) / [**Click Here to Listen**](https://drive.google.com/file/d/1a79y6Da4uIZN8yGpfmdE6yR1jOpyUqM1/view?usp=sharing) / [**Click Here to Present**](https://drive.google.com/file/d/1nC1PIH8bLwu21ePenIuQ35x-B7gbJ_qz/view?usp=sharing)

## Features

Aawaz comes packed with a variety of useful features:

* **Voice Interaction:** Communicates naturally using speech-to-text and text-to-speech.
* **Web Search:** fast searching on Google, YouTube, and Wikipedia via `SearchNow.py`.
* **News Updates:** Fetches and reads the latest headlines using `NewsRead.py`.
* **WhatsApp Automation:** Send messages automatically using voice commands via `Whatsapp.py`.
* **Translation:** Real-time language translation features via `Translator.py`.
* **Productivity Tools:**
    * **Focus Mode:** specialized mode to track and improve productivity (`FocusMode.py`, `FocusGraph.py`).
    * **Calculator:** Perform mathematical calculations via voice (`Calculatenumbers.py`).
    * **Dictionary:** Get definitions and meanings instantly (`Dictapp.py`).
    * **Alarm & Reminders:** Set alarms and reminders (`alarm.py`, `Remember.txt`).
* **Entertainment:** Built-in games and music playback (`game.py`, `music.mp3`).
* **System Control:** Keyboard automation and system tasks (`keyboard.py`).

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Key Libraries:**
    * `pyttsx3` (Text-to-Speech)
    * `speechRecognition` (Voice Input)
    * `pywhatkit` (Automation)
    * `wikipedia` (Information Retrieval)
    * `requests` (API Calls)
    * `googletrans` (Translation)

## 📥 Installation

Follow these steps to set up Aawaz on your local machine:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/haqorayush/Aawaz.git](https://github.com/haqorayush/Aawaz.git)
    cd Aawaz
    ```

2.  **Install Dependencies**
    The project includes an `Installer.py` script which is designed to help set up the necessary libraries. Run it to install the requirements automatically:
    
    ```bash
    python Installer.py
    ```

    *Alternatively, if you prefer to install manually, you likely need the following standard libraries:*
    ```bash
    pip install pyttsx3 speechRecognition pywhatkit wikipedia requests googletrans==4.0.0-rc1 playsound
    ```
    *(Note: You may need PyAudio. If `pip install pyaudio` fails, search for the specific wheel file for your OS).*

## Usage

1.  **Run the Assistant**
    Start the main application script:
    ```bash
    python Jarvis_main.py
    ```

2.  **Interact**
    Once the system initializes (you may hear a startup sound), speak your commands clearly.
    * *Example: "Wake up Jarvis"*
    * *Example: "Tell me the news"*
    * *Example: "Open YouTube"*

## Building an Executable

The repository includes a `Jarvis_main.spec` file, which indicates that you can bundle the application into a standalone `.exe` file using PyInstaller.

```bash
pip install pyinstaller
pyinstaller Jarvis_main.spec
```

The output file will be located in the dist folder.

## 🤝 Contributing
Contributions are welcome! If you'd like to improve Aawaz:

- Fork the repository.
- Create a new branch (git checkout -b feature/YourFeature).
- Commit your changes.
- Push to the branch.
- Open a Pull Request.

## License
This project is open-source. Please check the repository for specific license information.
