from flask import Flask, render_template, request
import speech_recognition as sr
import requests
from googletrans import Translator
import os
from werkzeug.utils import secure_filename
from datetime import datetime

# Add this import
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Get Monster API Key from environment variable
MONSTER_API_KEY = os.getenv('MONSTER_API_KEY')

# Initialize translator
translator = Translator()

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, couldn't understand the audio."
        except sr.RequestError as e:
            return f"API error: {e}"

def translate_to_english(text):
    translated = translator.translate(text, dest='en')
    return translated.text

def generate_image(prompt):
    url = "https://api.monsterapi.ai/v1/generate/txt2img"
    headers = {
        "Authorization": f"Bearer {MONSTER_API_KEY}"
    }
    payload = {
        "prompt": prompt,
        "model": "dreamshaper",
        "steps": 30,
        "cfg": 7,
        "seed": None,
        "aspect_ratio": "square"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        image_url = response.json()["output"][0]
        image_data = requests.get(image_url).content
        file_path = os.path.join("static", "output.png")
        with open(file_path, "wb") as f:
            f.write(image_data)
        return "output.png"
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    result_text = ""
    image_filename = None

    if request.method == "POST":
        if 'audio' not in request.files:
            result_text = "No file uploaded."
            return render_template("index.html", result=result_text)

        file = request.files['audio']
        if file.filename == '':
            result_text = "No file selected."
            return render_template("index.html", result=result_text)

        filename = secure_filename(f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        spoken_text = transcribe_audio(filepath)
        translated_prompt = translate_to_english(spoken_text)
        image_filename = generate_image(translated_prompt)

        if not image_filename:
            result_text = "Image generation failed. Try again."
        else:
            result_text = f"Prompt used: {translated_prompt}"

    return render_template("index.html", result=result_text, image=image_filename)

if __name__ == "__main__":
    app.run(debug=True)
