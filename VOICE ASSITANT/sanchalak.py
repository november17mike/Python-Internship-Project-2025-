import speech_recognition as sr
import pyttsx3
import re

# Import all feature modules
from speech_engine import speak
from voice_input import take_command
import check_weather
import reminder
import news_buff
import motivate_me

# Initialize the TTS engine globally
engine = pyttsx3.init()
engine.setProperty("rate", 165)

def speak(text):
    print(f"Orderly: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="en-in")
        print(f"You said: {command}")
    except Exception as e:
        print("SORRY SAAB! Could not understand audio.")
        return ""
    return command.lower()

def main():
    speak("JAI HIND SAAB! Orderly reporting for duty SAAB. How may I help?")

    while True:
        command = take_command()

        if not command:
            continue

        elif 'weather' in command:
            speak("Fetching the latest weather report SAAB!")
            default_city = "Bhubaneswar"

            # Extract city using regex
            city_search = re.search(r'weather in (.+)', command)
            if city_search:
                city = city_search.group(1).strip()
            else:
                city = default_city
            check_weather.get_weather(city)

        elif "reminder" in command:
            speak("What is the reminder, SAAB?")
            reminder_text = take_command()  # capture reminder text
            speak("When should I remind you? Give me a time value, like at '5 PM' or 'in 10 minutes'.")
            reminder_time = take_command()  # capture time
            reminder.set_reminder(reminder_text, reminder_time)


        elif "news" in command:
            speak("Fetching the latest news. Please wait.")
            news_buff.get_news()

        if "motivate" in command or "quote" in command:
            motivate_me.motivate()

        elif "exit" in command or "quit" in command or "dismiss" in command:
            speak("OK SAAB! Orderly signing off SAAB! JAI HIND SAAB!")
            break

        elif "stop listening" in command:
            speak("OK SAAB! I will remain silent until called again.")
            break

        else:
            speak("SORRY SAAB! I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    main()
