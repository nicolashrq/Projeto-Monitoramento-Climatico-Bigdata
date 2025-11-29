from ingestion.api_ingest import fetch_weather_data
from processing.clean import clean_weather_data
import pandas as pd
import os

# Buscar dados crus da API
raw = fetch_weather_data("Atibaia", -23.117, -46.550)

# Limpar dados
clean = clean_weather_data(raw)

print("Colunas retornadas pelo clean:", clean.keys())

# Criar pasta output se não existir
os.makedirs("output", exist_ok=True)

# Salvar em formato tabular (24 linhas)
df = pd.DataFrame({
    "city": clean["city"],
    "latitude": clean["latitude"],
    "longitude": clean["longitude"],
    "timestamp": clean["timestamps"],  # <-- clean.py usa timestamps (plural)
    "temperature": clean["temperature"],
    "humidity": clean["humidity"],
    "wind_speed": clean["wind_speed"]
})

df.to_csv(
    "output/Atibaia_clean.csv",
    index=False,
    encoding='utf-8-sig'
)

print("\nArquivo salvo em: output/Atibaia_clean.csv")


