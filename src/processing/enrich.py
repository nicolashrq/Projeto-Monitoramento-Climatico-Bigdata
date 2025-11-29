def enrich_weather_data(clean):
    temps = clean["temperature"]
    variations = [None]

    for i in range(1, len(temps)):
        variations.append(temps[i] - temps[i - 1])

    enriched = clean.copy()
    enriched["temp_variation"] = variations

    return enriched
