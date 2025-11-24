from ingestion.api_ingest import fetch_weather_data
from processing.clean import clean_weather_data
from processing.enrich import enrich_weather_data

raw = fetch_weather_data('Atibaia', -23.117, -46.550)
clean = clean_weather_data(raw)
enriched = enrich_weather_data(clean)

print(enriched.keys())
print("Primeiras variações:", enriched["temp_variation"][:10])
