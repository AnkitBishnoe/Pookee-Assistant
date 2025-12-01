import google.generativeai as genai

def aiProcess(command):
    # Configure the API key
    # Get your key from: https://aistudio.google.com/app/apikey
    # Replace the string below with your actual API key
    genai.configure(api_key="your api key")

    # Create the model
    model = genai.GenerativeModel("gemini-flash-latest")

    # Generate content
    try:
        response = model.generate_content(command)
        return response.text
    except Exception as e:
        return f"I apologize, but I encountered an error: {e}"
