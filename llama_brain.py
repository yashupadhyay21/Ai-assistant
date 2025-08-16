import subprocess

def ask_llama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3", prompt],
            capture_output=True,
            text=True,
            timeout=170
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Sorry, LLaMA took too long to respond."
    except Exception as e:
        return f"Error: {e}"
