import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the current Env
load_dotenv()

# Loading The API key from the env file
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("API key not found. Make sure to set the GOOGLE_API_KEY variable in the .env file.")

# configure the GenAI API Access modifier
genai.configure(api_key=GOOGLE_API_KEY)

# List the available genai libraries (gemni)
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)

# Select the model
model = genai.GenerativeModel('gemini-pro')

# Get response
try:
    prompt = input("Prompt: ")
    response = model.generate_content(prompt)
    print(response.text)

# If error occurs while getting response output error & prompt feedback
except ValueError as VE:
    print(f'Encountered {VE} looking at prompt details.\n')
    print(response.prompt_feedback)
