# === writer.py ===
import os
import requests
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

def ai_writer(text):
    prompt = f"Rewrite this in a more modern, engaging style:\n{text}"
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {groq_api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
    )
    
    try:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("❌ Groq API error response:")
        print(response.status_code)
        print(response.text)
        raise
