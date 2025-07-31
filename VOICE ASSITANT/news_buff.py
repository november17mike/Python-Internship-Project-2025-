import requests
import pyttsx3

API_KEY = "3d928852a99747b8b600cba64df961a9"

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)
    engine.say(text)
    engine.runAndWait()

def get_news():
    speak("Do you want national or international news?")
    choice = input("Enter your choice (national/international): ").strip().lower()

    country = "in" if choice == "national" else "us"  # Default to US for international

    speak("What kind of news are you looking for? Politics, sports, defence, entertainment or business?")
    category = input("Enter the category (politics/sports/defence/entertainment/business): ").strip().lower()

    speak("How many headlines do you want?")
    try:
        count = int(input("Enter number of headlines: ").strip())
    except ValueError:
        count = 5  # Default fallback
        speak("I'll give you 5 headlines by default.")

    # Special handling for 'defence' since it's not an official category
    if category == "defence":
        url = f"https://newsapi.org/v2/top-headlines?q=defence&country={country}&apiKey={API_KEY}&pageSize={count}"
    else:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={API_KEY}&pageSize={count}"

    print("Fetching news...")
    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] != "ok":
            print("Failed to fetch news")
            speak("Sorry, I was unable to fetch the news.")
            return

        articles = data.get("articles", [])
        if not articles:
            print("No articles found.")
            speak("Sorry, no articles were found in this category.")
            return

        speak(f"Here are your {count} {category} headlines.")
        for i, article in enumerate(articles[:count], start=1):
            title = article.get("title")
            if title:
                print(f"{i}. {title}")
                speak(title)

    except Exception as e:
        print("Error:", e)
        speak("There was an error while fetching the news.")
