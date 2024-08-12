import json
import os

PREFERENCES_FILE = os.path.join("data", "preferences.json")

def load_preferences():
    if os.path.exists(PREFERENCES_FILE):
        with open(PREFERENCES_FILE, "r") as file:
            data = json.load(file)
            return data.get("last_city")
    return None

def save_preferences(city):
    os.makedirs("data", exist_ok=True)
    with open(PREFERENCES_FILE, "w") as file:
        json.dump({"last_city": city}, file)
