import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 237)  # Speed
engine.setProperty('volume', 1)   # Volume


def text_to_speech(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()