# How Pookee Works

Welcome This document explains how your voice assistant, **Pookee**, works.

## Overview
Pookee is a voice-controlled assistant that follows a simple loop:
1.  **Listen**: Waits for a wake word (like "Hello" or "Pookee").
2.  **Acknowledge**: Responds with "Yes" to let you know it's ready.
3.  **Execute**: Listens for your command and performs the action.

---

## Key Components

### 1. Speaking (`speak` function)
- Converts text to speech using Google Text-to-Speech (gTTS).
- Plays the audio using **VLC Media Player**.
- **Important**: The program waits for the audio to finish playing before continuing. This ensures Pookee doesn't cut herself off.

### 2. Listening (`listen` function)
- Uses the microphone to capture audio.
- Adjusts for background noise automatically.
- Converts speech to text using Google's Speech Recognition API.

### 3. Processing Commands (`processcommand` function)
- **Web Commands**: Opens Google, YouTube, Facebook, or Instagram.
- **Music**: Plays songs from your `musiclibrary.py` file (e.g., "play skyfall").
- **AI Chat**: If the command isn't recognized, it sends the query to Gemini AI for a smart response.

---

## How to Run
1.  Ensure you have Python and VLC installed.
2.  Navigate to the `program_come` directory:
    ```bash
    cd "c:\Users\DELL\OneDrive\Desktop\pyton\cb project\program_come"
    ```
3.  Run the script:
    ```bash
    python main.py
    ```
4.  Say **"Hello"** or **"Pookee"** to start.

