# main.py

import speech_recognition as sr
import pyttsx3
import webbrowser

from wakeword.wakeword_listener import listen_for_wake_word
from brain import generate_response_ollama

# Initialize text-to-speech engine
tts = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print(f"💬 DEMON: {text}")
    tts.say(text)
    tts.runAndWait()

def get_voice_command():
    with sr.Microphone() as source:
        print("🎙️ Listening for your command...")
        audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio)
            print(f"🗣️ You: {query}")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""

def main():
    while True:
        listen_for_wake_word()  # Blocks until wake word is heard
        speak("Yes, Yash?")
        command = get_voice_command()

        if not command:
            continue

        if "exit" in command.lower() or "shutdown" in command.lower():
            speak("Shutting down. Goodbye.")
            break

        response = generate_response_ollama(command)
        speak(response)

        # Optional: Automatically open web if "open" mentioned
        if "open" in command.lower():
            webbrowser.open(f"https://www.google.com/search?q={command}")

if __name__ == "__main__":
    main()
