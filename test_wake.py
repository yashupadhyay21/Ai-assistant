from wakeword.wakeword_listener import listen_for_wake_word
from speak import speak
from llama_brain import ask_llama
from command_router import handle_command
import speech_recognition as sr

def listen_for_question():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for your question...")
        speak("What would you like to do?")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        return "I couldn't understand what you said."
    except sr.RequestError:
        return "Speech recognition service is unavailable."

print("🎧 Say 'Demon' to activate...")

while True:
    listen_for_wake_word()
    speak("Yes, I am listening.")
    
    user_prompt = listen_for_question()
    if not user_prompt:
        continue

    # Try browser command first
    browser_result = handle_command(user_prompt)
    if browser_result:
        print(f"🌐 DEMON: {browser_result}")
        speak(browser_result)
        continue

    # Else: Send to LLaMA
    response = ask_llama(user_prompt)
    print(f"🤖 DEMON: {response}")
    speak(response)
