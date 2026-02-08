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
COORDINATES_PATH = CONFIGS_DIR / "coordinates.csv"
RAW_FORECASTS_PATH = RAW_DATA_DIR / "forecasts.json"
TRANSFORMED_FORECASTS_PATH = TRANSFORMED_DATA_DIR / "forecasts.parquet"

# API URLs, endpoints and query parameters
FORECAST_URL="https://api.open-meteo.com"
FORECASTS_ENDPOINT="/v1/forecast"
FORECAST_DAYS=14

# Temperature unit and timezone are not necessary, since unit resolves to Celsius by default
# and timezone resolves to the local timezone. See the docs at: https://open-meteo.com/en/docs?location_mode=csv_coordinates 
# HOURLY_VARIABLES="temperature_2m,temperature_2m_max,temperature_2m_min,precipitation_probability,precipitation"
HOURLY_VARIABLES="temperature_2m,precipitation_probability,precipitation"

