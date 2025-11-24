from ingestion.api_ingest import fetch_weather_data
from processing.clean import clean_weather_data
from processing.enrich import enrich_weather_data
from aggregation.metrics import compute_city_metrics
from utils.helpers import save_json

cities = {
    "São Paulo": (-23.55, -46.63),
    "Rio de Janeiro": (-22.90, -43.20),
    "Atibaia": (-23.117, -46.550)
}

def run_pipeline():
    results = []
    
    for city, (lat, lon) in cities.items():
        print(f"\n Iniciando ingestão de {city}...")
        
        raw = fetch_weather_data(city, lat, lon)
        clean = clean_weather_data(raw)
        enriched = enrich_weather_data(clean)
        metrics = compute_city_metrics(enriched)

        results.append(metrics)
        save_json(f"output/{city.replace(' ', '_')}.json", enriched)

        print(f" {city} processado")

    print("\n Métricas finais:")
    for r in results:
        print(r)

if __name__ == "__main__":
    run_pipeline()
