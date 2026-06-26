import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city="Malda"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": "metric"
        }
        response = requests.get(url, params=params)
        data = response.json()

        weather = {
            "city": city,
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather

    except Exception as e:
        return {"error": str(e)}

def format_weather(city="Malda"):
    w = get_weather(city)
    if "error" in w:
        return f"⚠️ Could not fetch weather: {w['error']}"
    return (
        f"🌤 *Weather in {w['city']}*\n"
        f"🌡 Temp: {w['temp']}°C (feels like {w['feels_like']}°C)\n"
        f"💧 Humidity: {w['humidity']}%\n"
        f"🌬 Wind: {w['wind_speed']} m/s\n"
        f"☁️ {w['description'].capitalize()}"
    )
