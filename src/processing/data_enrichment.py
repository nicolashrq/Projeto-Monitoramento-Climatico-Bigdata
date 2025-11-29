# src/processing/data_enrichment.py

def enrich_weather_data(raw):
    """
    Recebe os dados crus vindos da API e garante que TODAS as colunas
    necessárias existam, evitando KeyError.
    """

    enriched = {
        "city": raw.get("city", ""),
        "temperature": raw.get("temperature"),
        "humidity": raw.get("humidity"),
        "wind_speed": raw.get("wind_speed"),
        "timestamp": raw.get("timestamp")
    }

    # Exemplo de métrica derivada
    if enriched["temperature"] is not None and enriched["humidity"] is not None:
        enriched["heat_index"] = enriched["temperature"] + (0.1 * enriched["humidity"])
    else:
        enriched["heat_index"] = None

    return enriched
