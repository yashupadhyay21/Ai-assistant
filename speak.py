import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)  # Adjust speech speed (default ~200)
    engine.setProperty('volume', 1.0)  # Max volume
    voices = engine.getProperty('voices')
    
    # Optional: Choose a deeper/clearer voice
    engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)

    engine.say(text)
    engine.runAndWait()
