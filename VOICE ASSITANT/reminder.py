# reminder.py

import threading
import time
from datetime import datetime

reminders = []

def set_reminder(reminder_text, reminder_time):
    """
    reminder_text: str - what to remind
    reminder_time: datetime - when to remind
    """
    reminders.append((reminder_text, reminder_time))
    print(f"Reminder set: '{reminder_text}' at {reminder_time.strftime('%H:%M')}")

def check_reminders(speak_func):
    """
    Continuously check reminders in background and speak when reminder time matches
    speak_func: function to convert text to speech (e.g., speak from speech_engine.py)
    """
    def run():
        while True:
            now = datetime.now()
            for reminder in reminders[:]:
                text, remind_time = reminder
                if now >= remind_time:
                    speak_func(f"Reminder: {text}")
                    reminders.remove(reminder)
            time.sleep(30)  # check every 30 seconds

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
