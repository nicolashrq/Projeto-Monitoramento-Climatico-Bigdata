from ingestion.api_ingest import fetch_weather_data
from processing.clean import clean_weather_data
from processing.enrich import enrich_weather_data
import pandas as pd
import os

# Buscar > limpar > enriquecer
raw = fetch_weather_data('Atibaia', -23.117, -46.550)
clean = clean_weather_data(raw)
enriched = enrich_weather_data(clean)

print("Colunas geradas pelo enrich:", enriched.keys())
print("Primeiras variações:", enriched["temp_variation"][:10])

# Criar pasta output
os.makedirs("output", exist_ok=True)

# Descobrir automaticamente se é "timestamp" ou "timestamps"
timestamps_key = "timestamp" if "timestamp" in enriched else "timestamps"

df = pd.DataFrame({
    "city": enriched["city"],
    "latitude": enriched["latitude"],
    "longitude": enriched["longitude"],
    "timestamp": enriched[timestamps_key],
    "temperature": enriched["temperature"],
    "humidity": enriched["humidity"],
    "wind_speed": enriched["wind_speed"],
    "temp_variation": enriched["temp_variation"],
    "humidity_variation": enriched["humidity_variation"],
    "wind_variation": enriched["wind_variation"]
})

df.to_csv(
    "output/Atibaia.csv",
    index=False,
    encoding='utf-8-sig'
)

print("\nArquivo salvo em: output/Atibaia.csv")


