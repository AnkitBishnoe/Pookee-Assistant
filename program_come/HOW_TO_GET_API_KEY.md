# How to Get a Google Gemini API Key

To make the AI features work, you need your own API key from Google. It is free and easy to get.

1.  **Go to Google AI Studio**:
    Click this link: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

2.  **Sign In**:
    Sign in with your Google account.

3.  **Create Key**:
    Click on **"Create API key"**.
    You can choose "Create API key in new project".

4.  **Copy the Key**:
    You will see a long string of characters starting with `AIza...`. Copy this string.

5.  **Paste in Code**:
    Open the file `client.py` in your project.
    Find the line that looks like:
    `genai.configure(api_key="PASTE_YOUR_API_KEY_HERE")`
    Replace `PASTE_YOUR_API_KEY_HERE` with the key you copied.

    **Example:**
    `genai.configure(api_key="AIzaSyB...")`

6.  **Save and Run**:
    Save the file and run `main.py` again.
