def clean_weather_data(raw):
    hourly = raw["hourly"]

    clean = {
        "city": raw["city"],
        "latitude": raw["lat"],
        "longitude": raw["lon"],
        "timestamp": hourly["time"],
        "temperature": hourly["temperature_2m"]
    }

    return clean
