# Python-Internship-Project-2025-
A collection of Python-based internship projects including an AI grammar checker (Studdy_Buddy), a voice-activated personal assistant for soldiers (Orderly), and a speech-to-image generator (Speech_2_Img), built using Flask, NLP, and MonsterAPI.

*Note- This repository contains a collection of Python-based projects developed during my internship in 2025. Each project demonstrates practical application of Python, AI/ML concepts, APIs, and deployment tools.*

## Projects Includes:
1. **Studdy_Buddy**  
   An intelligent writing assistant that analyzes user-entered English text for:
   - **Grammar issues**
   - **Spelling errors**
   - **Sentiment polarity**
   - **Subjectivity**
   - Also highlights negative expressions and suggests positive rewrites.

2. **Orderly (Voice-Activated Personal Assistant)**  
   Inspired by Tony Stark’s J.A.R.V.I.S., **Orderly** is a modular voice assistant with military-style language and multiple capabilities:
   - Weather reports
   - News reading
   - Setting reminders
   - Motivational quotes
   - Military facts
   - Offline + Online hybrid voice engine
   - Interactive command recognition using speech

3. **Speech 2 Img**  
   A multilingual speech-to-image generator that:
   - Takes voice input in any language
   - Translates it to English
   - Uses Stable Diffusion via MonsterAPI to generate creative images
   - Features a Flask-based web interface


## Tools & Technologies Used
- **Python**
- **Flask**
- **SpeechRecognition**
- **TextBlob**
- **LanguageTool**
- **Googletrans**
- **Pyttsx3 / Edge-TTS**
- **OpenWeatherMap API, NewsAPI**
- **MonsterAPI (for Diffusion)**
- **HTML/CSS/JS for Web UI**
- **.env for API management**
- **Virtual Environments**
- **Git & GitHub**


## Project Folder Structure
Projects│
├── Studdy_Buddy/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   ├── .env
│   ├── README.md
│   └── requirements.txt
│
├── Orderly/
│   ├── sanchalak.py
│   ├── features/
│   ├── data/
│   ├── utils/
│   ├── .env
│   ├── README.md
│   └── requirements.txt
│
├── Speech_2_Img/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   ├── uploads/
│   ├── .env
│   ├── README.md
│   └── requirements.txt
│
├── .gitignore
└── README.md ← (this file)


**How to Run the Projects:**
# Clone this repository
git clone https://github.com/your-username/Internship-Projects-2025.git
cd Internship-Projects-2025/ProjectName/*

# Set up virtual environment:
python -m venv venv
venv\Scripts\activate   # On Windows

# Install dependencies:
pip install -r requirements.txt
Add your .env file with valid API keys where needed.

# Run the app (web or terminal depending on project):
python app.py


## Future Enhancements:
1. Deploy Studdy_Buddy and Speech 2 Img on Render or Railway
2. Integrate more languages and accents in Orderly’s recognition system.
3. Add mobile responsiveness and UX improvements in the UI-based apps.
4. Dockerize the applications for seamless deployment.

## My Experience with CodeXInterns:
This internship strengthened my practical command of Python, NLP, speech tech, and API-driven app development.
To explore the projects in detail please surf through the folders for detailed implementations and README guides.

