import requests
import json
import os
from datetime import datetime, timezone

# === CONFIG ===
WEATHER_API_KEY = os.getenv("API_KEY")  # Get API key from environment variable
CITY = "Mawsynram"
OUTPUT_FILE = "weather.json"

if not WEATHER_API_KEY:
    raise ValueError("Missing API_KEY environment variable")

# === Fetch weather data ===
url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={CITY}"
response = requests.get(url)

if response.status_code != 200:
    exit(1)

data = response.json()

# === Prepare simplified JSON ===
weather_summary = {
    "city": CITY,
    "condition": data["current"]["condition"]["text"],
    "updated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
}

# === Write to file ===
with open(OUTPUT_FILE, "w") as f:
    json.dump(weather_summary, f, indent=2)

