Speech 2 Img - Multilingual Speech-to-Image Generator

##Project Objective:
-Speech 2 Img is a web application that captures multilingual audio input and uses it to generate descriptive images using MonsterAPI’s text-to-image generation model.

#Tools & Technologies Used:

1. Python
2. Flask
3. SpeechRecognition
4. OpenAI Whisper (optional upgrade)
5. MonsterAPI (Diffusers based image generation)
6. HTML/CSS (Frontend)
7. dotenv (.env for API key handling)


#Features:

1. Accepts audio input from user
2. Converts speech to text using SpeechRecognition
3. Sends transcription to MonsterAPI for image generation
4. Displays output image to user
5. Supports multiple languages


#How to Run:

1. Clone the repo
2. Set up a .env file with MonsterAPI key
3. Run app.py
4. Use microphone to input a sentence, get a generated image


#Future Enhancements:

1. Whisper integration for higher accuracy transcription
2. Image quality selector
3. Language selector dropdown
4. Deployment for global use
5. Mobile responsiveness

