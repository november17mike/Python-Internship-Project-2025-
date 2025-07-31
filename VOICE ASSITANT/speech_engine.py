import asyncio
import os
import uuid
import socket

try:
    import edge_tts
except ImportError:
    edge_tts = None

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

def is_connected(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception:
        return False

async def speak_edge(text):
    filename = f"temp_{uuid.uuid4().hex}.mp3"
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-IN-NeerjaNeural",
        rate="+30%"
    )
    await communicate.save(filename)
    os.system(f'start {filename}')

def speak_pyttsx3(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def speak(text):
    # Print the text exactly as Orderly would say it, preserving style
    print(f"Orderly: {text}")

    if edge_tts and is_connected():
        try:
            asyncio.run(speak_edge(text))
            return
        except Exception as e:
            print(f"[edge-tts error] Falling back to pyttsx3: {e}")

    if pyttsx3:
        speak_pyttsx3(text)
    else:
        print("No TTS engine available. Please install edge-tts or pyttsx3.")
