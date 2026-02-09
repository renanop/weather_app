from pathlib import Path
from weather_app.schemas import APIConfig


# API config object necessary to request the open meteo api
REQUEST_FORECASTS_CONFIG = APIConfig(
    url="https://api.open-meteo.com/",
    endpoint="/v1/forecast",
    days=14,
    hourly_vars="temperature_2m,precipitation_probability,precipitation"
)
# Root path
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Configs folder
CONFIGS_DIR = PROJECT_ROOT / "configs"

# Data folder
DATA_DIR = PROJECT_ROOT / "data"

## Raw data
RAW_DATA_DIR = DATA_DIR / "raw"

## Transformed data
TRANSFORMED_DATA_DIR = DATA_DIR / "transformed"

## Refined data
REFINED_DATA_DIR = DATA_DIR / "refined"

# Important file pathes
COORDINATES_PATH = CONFIGS_DIR / "coordinates.csv"
RAW_FORECASTS_PATH = RAW_DATA_DIR / "forecasts.json"
TRANSFORMED_FORECASTS_PATH = TRANSFORMED_DATA_DIR / "forecasts.parquet"


