import os
from dotenv import load_dotenv
import google.generativeai as genai


def configure_genai():
    # Load the current Env
    load_dotenv()

    # Loading The API key from the env file
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    if not GOOGLE_API_KEY:
        raise ValueError("API key not found. Make sure to set the GOOGLE_API_KEY variable in the .env file.")

    # configure the GenAI API Access modifier
    genai.configure(api_key=GOOGLE_API_KEY)


def list_genai_models():
    # List the available genai libraries (gemni)
    models = [m.name for m in genai.list_models() if "generateContent" in m.supported_generation_methods]
    return models


def generate_response(prompt):
    # Select the model
    model = genai.GenerativeModel('gemini-pro')

    try:
        response = model.generate_content(prompt)
        return response.text

    except ValueError as VE:
        return f'Encountered {VE} looking at prompt details.\n'
