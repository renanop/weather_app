from pathlib import Path

# Defining useful pathes
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Folders
CONFIGS_DIR = PROJECT_ROOT / "configs"
DATA_DIR = PROJECT_ROOT / "data"

## Raw 
RAW_DATA_DIR = DATA_DIR / "raw"
RAW_FORECASTS_DIR = RAW_DATA_DIR / "forecasts"

## Transformed data
TRANSFORMED_DATA_DIR = DATA_DIR / "transformed"

## Refined data
REFINED_DATA_DIR = DATA_DIR / "refined"

# Important file pathes
COORDINATES_PATH = CONFIGS_DIR / "coordinates.json"

# API URLs, endpoints and query parameters
FORECAST_URL="https://api.open-meteo.com"
FORECASTS_ENDPOINT="/v1/forecast"
FORECAST_DAYS=14
HOURLY_VARIABLES="temperature_2m,precipitation_probability,precipitation"

