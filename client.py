import google.generativeai as genai

# Configure the API key
genai.configure(api_key="YOUR_API_KEY_HERE")

def aiProcess(command):
    """Process command using Gemini AI."""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(command)
    return response.text
