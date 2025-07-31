import requests
from speech_engine import speak

API_KEY = "6a96eecf0ee4adc1b9b6ae3241c38396"  # Replace with your actual OpenWeatherMap API key

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] != 200:
            speak(f"Sorry SAAB! I couldn't find the weather for {city}.")
            return

        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_report = (
            f"Current weather in {city}: {weather_desc}. "
            f"The temperature is {temp} degree Celsius, "
            f"humidity is {humidity} percent, "
            f"and wind speed is {wind_speed} meters per second."
        )

        speak(weather_report)

    except Exception as e:
        speak("Sorry SAAB, I am unable to get the weather right now.")
        print(f"[Weather Module Error]: {e}")
