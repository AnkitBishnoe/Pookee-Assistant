import speech_recognition as sr
import re
import webbrowser
import os
from gtts import gTTS
import musiclibrary
import client

# ----------------- TTS FUNCTION -----------------
def clean_text(text):
    """Removes special characters for better TTS."""
    cleaned = re.sub(r'[^a-zA-Z0-9\s.,?!]', '', text)
    return cleaned

def speak(text):
    print("Speaking:", text)
    
    cleaned_text = clean_text(text)
    if not cleaned_text.strip():
        return

    try:
        filename = "voice.mp3"
        tts = gTTS(text=cleaned_text, lang='en')
        tts.save(filename)
        
        # Play audio with VLC and wait for completion
        os.system(f'start /wait /min vlc --intf dummy --play-and-exit "{filename}"')

        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:
        print("TTS Error:", e)


# ----------------- LISTEN FUNCTION -----------------
recognizer = sr.Recognizer()

def listen(timeout=4, limit=6):
    """Listens to microphone and converts speech to text."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")

        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=limit)
            text = recognizer.recognize_google(audio)
            print("Heard:", text)
            return text.lower()

        except Exception as e:
            print("Listen Error:", e)
            return ""


# ----------------- COMMAND PROCESSOR -----------------
def processcommand(cmd):
    cmd = cmd.lower()

    # Website commands
    sites = {
        "google": "https://google.com",
        "youtube": "https://youtube.com",
        "facebook": "https://facebook.com",
        "instagram": "https://instagram.com",
        "insta": "https://instagram.com"
    }
    
    for site, url in sites.items():
        if f"open {site}" in cmd:
            speak(f"Opening {site.capitalize()}")
            webbrowser.open(url)
            return

    if cmd.startswith("play"):
        try:
            song = cmd.split(" ")[1]
            speak(f"Playing {song}")
            webbrowser.open(musiclibrary.music[song])
        except:
            speak("I could not find that song.")
        return

    # AI fallback
    try:
        speak("Processing your request")
        output = client.aiProcess(cmd)
        print("Gemini:", output)
        speak(output)
    except Exception as e:
        print("Gemini Error:", e)
        speak("I could not process your request.")


# ----------------- MAIN LOOP -----------------
if __name__ == "__main__":
    print("Starting Pookee...")
    speak("Initializing Pookee")

    while True:
        print("\nWaiting for wake word...")
        wake = listen(timeout=6, limit=3)

        if any(w in wake for w in ["hello", "hey", "pookie", "pookee"]):
            speak("yes")
            print("Wake word detected!")

            speak("Listening for your command...")
            command = listen(timeout=7, limit=7)

            if command != "":

                processcommand(command)
