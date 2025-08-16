# GPT communication logic
# brain.py
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

def generate_response_ollama(query):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3",
        "messages": [
            {"role": "user", "content": query}
        ]
    }

    try:
        response = requests.post(OLLAMA_URL, json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result["message"]["content"]
    except Exception as e:
        return f"Error from LLaMA: {e}"
