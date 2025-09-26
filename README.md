 
# Jarvis Voice Assistant

A Python-based voice assistant that listens for a wake word, executes commands, plays music, opens websites, and fetches news headlines.
(Important note: right now it just performs basic tasks specified by me; you can optimize it as per your requirement)

 

## Features

- **Wake word activation:** Start Jarvis by saying “Hello Jarvis”, “Hi Jarvis”, or “Jarvis”.
Once Jarvis is activated, you can now ask it to perform the tasks.
- **Website launching:** speak these for website launching: Open YouTube, Google, LinkedIn, Facebook, Pinterest, Spotify, or your personal LinkedIn page.
(Make sure you speak the word open and the page name that you want to open properly)
- **Music playback:** Play English songs or themed playlists like workout, study, relaxation, drive, and party.
- **News headlines:** Fetch top headlines from NewsAPI. Speak the number of headlines you want (supports numbers in digits and words, e.g., “5” or “five”).
(right now just programmed to fetch the general news )
- **Continuous command mode:** Stay active until the user says “exit”, “stop”, or similar commands. 
- **Logout and shutdown commands:** Say “logout”, “sleep”, “bye Jarvis”, etc., to exit completely.

 

## Requirements

- Python 3.10+
- Packages: speechrecognition, pyttsx3, requests, pyaudio

```bash
pip install speechrecognition pyttsx3 requests pyaudio
````

> **Note:** `pyaudio` may require system-specific installation instructions. On Windows, you can use:
>
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

* `musiclib.py` – a custom module containing URLs for music playlists. You can add the URLs of the music you want.

---

## Setup

1. Clone or download the project folder.
2. Create a virtual environment (recommended):

```bash
python -m venv venv
```

3. Activate the environment:

```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
.\venv\Scripts\activate.bat
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Replace `API_KEY` in your `main.py` with your NewsAPI key. (create a developer account in NewsAPI)

---

## Usage

1. Run the main Python script:

```bash
python main.py
```

2. Speak the **wake word** to activate Jarvis:

```
"Hello Jarvis" / "Hi Jarvis" / "Jarvis"
```

3. Give commands, for example:

* **Open websites:**

```
open youtube
open linkedin
open my LinkedIn page
```

* **Play music:**

```
play workout
play study
play random
```

* **Fetch news:**

```
news or headlines - these keywords should be present
```

Then speak the number of headlines you want, e.g., "5" or "five".

4. To exit command mode:

```
exit / stop
```

5. To shutdown Jarvis completely:

```
logout / sleep / bye Jarvis
```

---

## Example Commands

```text
"Open Google"
"Play workout playlist"
"Show top news"
"Exit"
"Logout"
```

---

## Notes

* Works best in quiet environments.
* Recognizes numbers both as digits (“5”) and words (“five”).
* Ensure a working microphone is connected.

---

## Future Enhancements

* Integrate more voice commands like reminders, weather, and calculator.
* Add AI responses using OpenAI GPT API.
* Enhance music playback with Spotify API integration.

 
 
