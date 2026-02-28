import argparse
from weather_app.configs import (
    COORDINATES_PATH, 
    RAW_ACTUALS_PATH, 
    REQUEST_ACTUALS_CONFIG, 
    RETRY_STRATEGY
)
from weather_app.pipelines.ingest.engine import run_weather_ingestion

def main() -> None:
    """Entry point for the actuals (historical) ingestion pipeline."""
    parser = argparse.ArgumentParser(description="Fetch historical weather data.")
    parser.add_argument("--start-date", type=str, help="Start date in YYYY-MM-DD format")
    parser.add_argument("--end-date", type=str, help="End date in YYYY-MM-DD format")
    
    args = parser.parse_args()

    run_weather_ingestion(
        coordinates_path=COORDINATES_PATH,
        output_path=RAW_ACTUALS_PATH,
        config=REQUEST_ACTUALS_CONFIG,
        retry_strategy=RETRY_STRATEGY,
        start_date=args.start_date,
        end_date=args.end_date
    )

if __name__ == '__main__':
    main()
