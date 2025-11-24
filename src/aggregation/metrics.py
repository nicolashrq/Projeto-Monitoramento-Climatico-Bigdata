def compute_city_metrics(cleaned):
    temps = cleaned["temperature"]
    return {
        "city": cleaned["city"],
        "min_temp": min(temps),
        "max_temp": max(temps),
        "avg_temp": sum(temps)/len(temps)
    }
