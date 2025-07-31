import random
from speech_engine import speak

quotes = [
    "If a man says he is not afraid of dying, he is either lying or is a Gorkha. — Field Marshal Sam Manekshaw",
    "The soldier is the Army. No army is better than its soldiers. — General George S. Patton",
    "Courage is fear holding on a minute longer. — General George S. Patton",
    "Discipline is the soul of an army. It makes small numbers formidable; procures success to the weak, and esteem to all. — George Washington",
    "The more you sweat in peace, the less you bleed in war. — Norman Schwarzkopf",
    "Victory belongs to the most persevering. — Napoleon Bonaparte",
    "An army marches on its stomach. — Napoleon Bonaparte",
    "The harder the conflict, the greater the triumph. — George Washington",
    "Bravery is being the only one who knows you’re afraid. — Colonel David Hackworth",
]

facts = [
    "The Indian Army is the third-largest standing army in the world with over 1.2 million active personnel.",
    "The Gorkha Regiment is famous worldwide for its bravery and the unique Kukri knife.",
    "The Indian Army celebrates Army Day every year on January 15th, commemorating when General K. M. Cariappa took over as the first Indian Commander-in-Chief in 1949.",
    "The highest military award in India is the Param Vir Chakra.",
    "India's Special Forces include the Para SF, MARCOS, and Garud Commandos.",
    "The Indian Army has participated in UN peacekeeping missions across the globe since 1958.",
]

war_facts = [
    "In 1947-48, India fought its first war with Pakistan over Kashmir after independence, leading to the establishment of the Line of Control.",
    "The 1947-48 Kashmir war was fought in harsh winter conditions with newly formed Indian Army units.",
    "The 1962 Sino-Indian War was a brief but intense conflict where India faced China over disputed Himalayan borders.",
    "Despite setbacks in 1962, the war led to modernization and restructuring of the Indian Army.",
    "The 1965 war with Pakistan was triggered by infiltration attempts in Kashmir and saw large tank battles like the Battle of Asal Uttar.",
    "The Indian Army showcased strong defensive and offensive operations, successfully repelling Pakistani advances.",
    "The 1971 war led to the creation of Bangladesh and is considered one of India’s most decisive military victories.",
    "Under General Manekshaw’s leadership, the Indian Army conducted successful coordinated operations on both Eastern and Western fronts.",
    "The Kargil War was fought in 1999 in high-altitude mountains where Indian soldiers recaptured strategic peaks from infiltrators.",
    "Operation Vijay was launched to evict Pakistani forces from Kargil heights, showcasing exceptional bravery in tough terrain.",
]

def motivate():
    quote = random.choice(quotes)
    fact = random.choice(facts + war_facts)
    combined_message = f"Motivational Quote: {quote}\nArmy Fact: {fact}"
    print(f"{combined_message}")
    # Speak both parts separately for better clarity
    speak("Sure SAAB! Motivation for the day.")
    speak(quote)
    speak(f"Did you know? {fact}")
