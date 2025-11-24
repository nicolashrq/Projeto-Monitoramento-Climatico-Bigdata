def clean_weather_data(raw):
    hourly = raw["data"]["hourly"]
    df = {
        "city": raw["city"],
        "latitude": raw["lat"],
        "longitude": raw["lon"],
        "timestamps": hourly["time"],
        "temperature": hourly["temperature_2m"]
    }
    return df
