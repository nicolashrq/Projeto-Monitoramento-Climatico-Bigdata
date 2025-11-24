def enrich_weather_data(cleaned):
    temps = cleaned["temperature"]
    diffs = [None] + [temps[i] - temps[i-1] for i in range(1, len(temps))]
    cleaned["temp_variation"] = diffs
    return cleaned
