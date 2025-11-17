import pyttsx3

def get_best_voice(engine):
    """Automatically select the most natural-sounding voice available."""
    voices = engine.getProperty('voices')
    best_voice = voices[0]  # Default fallback

    # Keywords that hint at more natural voices
    preferred_keywords = ["zira", "aria", "eva", "en_us", "female", "english", "neural"]

    for voice in voices:
        name_lower = voice.name.lower()
        if any(keyword in name_lower for keyword in preferred_keywords):
            best_voice = voice
            break

    return best_voice


# --- Initialize engine ---
engine = pyttsx3.init()

# --- Tune for natural speech ---
engine.setProperty('rate', 155)      # Speed of voice (lower = calmer)
engine.setProperty('volume', 0.9)    # Volume (0.0 to 1.0)

# --- Pick the most human-like voice ---
chosen_voice = get_best_voice(engine)
engine.setProperty('voice', chosen_voice.id)

print(f"🎙️ Using voice: {chosen_voice.name}")

# --- Lines your robot will say ---
lines = [
    "This is a basic idea of robot speech.",
    "Obstacle detected... changing the path.",
    "I see something ahead!"
]

# --- Queue all lines together ---
for line in lines:
    engine.say(line)

# --- Speak them smoothly ---
engine.runAndWait()

# By AI