import os
import re
import google.generativeai as genai
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

genai.configure(api_key=API_KEY)

def clean_sql(response: str) -> str:
    """
    Extracts valid SQL from Gemini response, removing markdown and explanations.
    """
    if not response:
        return ""
    match = re.search(r"```sql\s*(.*?)```", response, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return response.strip()

@retry(stop=stop_after_attempt(3), wait=wait_exponential())
def chat(system: str, user: str) -> str:
    model = genai.GenerativeModel(MODEL)
    prompt = f"{system.strip()}\n\nUser query: {user.strip()}"
    resp = model.generate_content(prompt)
    return clean_sql(resp.text)
