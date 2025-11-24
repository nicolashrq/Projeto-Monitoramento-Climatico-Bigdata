import requests
import json

def fetch_weather_data(city: str, lat: float, lon: float):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    return {"city": city, "lat": lat, "lon": lon, "data": data}