# voice_input.py

import speech_recognition as sr

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return "SORRY SAAB! I did not understand that."
        except sr.RequestError:
            return "SORRY SAAB! Service is down. Please try again later."
