import requests
import json
from datetime import datetime, timezone

# === CONFIG ===
WEATHER_API_KEY = "e5731ee06a654499b9e42608250906"  
CITY = "Mawsynram"
OUTPUT_FILE = "weather.json"

# === STEP 1: Fetch weather data ===
url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={CITY}"
response = requests.get(url)

if response.status_code != 200:
    exit(1)

data = response.json()

# === STEP 2: Prepare simplified JSON ===
weather_summary = {
    "city": CITY,
    "condition": data["current"]["condition"]["text"],
    "updated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

}

# === STEP 3: Write to file ===
with open(OUTPUT_FILE, "w") as f:
    json.dump(weather_summary, f, indent=2)

