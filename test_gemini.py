import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load env vars from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ No API key found. Please set GEMINI_API_KEY in .env")

# Configure Gemini
genai.configure(api_key=api_key)

# Pick a lightweight model
model = genai.GenerativeModel("gemini-1.5-flash")

# Test prompt
response = model.generate_content("Hello Gemini! Can you confirm you're alive?")

print("Gemini says:", response.text)
