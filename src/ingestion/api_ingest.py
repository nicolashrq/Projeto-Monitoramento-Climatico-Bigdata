import requests

def fetch_weather_data(city: str, lat: float, lon: float):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&hourly=temperature_2m"
    )

    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()

    # Garantindo que volte no formato certo
    return {
        "city": city,
        "lat": lat,
        "lon": lon,
        "hourly": data["hourly"]   # <-- AGORA É CERTO
    }
