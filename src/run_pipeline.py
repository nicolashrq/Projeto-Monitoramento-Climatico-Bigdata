from ingestion.api_ingest import fetch_weather_data
from processing.clean import clean_weather_data
from processing.enrich import enrich_weather_data
import pandas as pd
import os


# Cidades usadas no pipeline
cities = {
    "São Paulo": (-23.55, -46.63),
    "Rio de Janeiro": (-22.90, -43.20),
    "Atibaia": (-23.117, -46.550)
}


# Função para calcular métricas da cidade (min, max, média)
def compute_city_metrics(enriched):
    temps = enriched["temperature"]
    return {
        "city": enriched["city"],
        "min_temp": min(temps),
        "max_temp": max(temps),
        "avg_temp": sum(temps) / len(temps)
    }


def run_pipeline():
    os.makedirs("output", exist_ok=True)
    metrics_results = []

    for city, (lat, lon) in cities.items():
        print(f"\nIniciando ingestão de {city}...")

        # 1. Coleta
        raw = fetch_weather_data(city, lat, lon)

        # 2. Limpeza
        clean = clean_weather_data(raw)

        # 3. Enriquecimento
        enriched = enrich_weather_data(clean)

        # 4. Métricas
        metrics = compute_city_metrics(enriched)
        metrics_results.append(metrics)

        # 5. Salvar CSV
        df = pd.DataFrame({
            "timestamp": enriched["timestamp"],
            "temperature": enriched["temperature"],
            "temp_variation": enriched["temp_variation"],
            "city": [city] * len(enriched["timestamp"]),
            "latitude": [lat] * len(enriched["timestamp"]),
            "longitude": [lon] * len(enriched["timestamp"])
        })

        csv_path = f"output/{city.replace(' ', '_')}.csv"
        df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        print(f"Arquivo salvo em: {csv_path}")

        print(f"{city} processado")


    # Mostrar métricas no final
    print("\nMétricas finais:")
    for m in metrics_results:
        print(m)


if __name__ == "__main__":
    run_pipeline()
