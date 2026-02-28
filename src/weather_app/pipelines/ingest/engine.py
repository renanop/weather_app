from pathlib import Path
import pandas as pd
from weather_app.utils.readers import request_api
from weather_app.utils.wrangling import join_column_text
from weather_app.utils.writers import save_json
from weather_app.schemas import APIConfig, RetryStrategy

def run_weather_ingestion(
    coordinates_path: Path,
    output_path: Path,
    config: APIConfig,
    retry_strategy: RetryStrategy,
    start_date: str | None = None,
    end_date: str | None = None,
    days: int | None = None
) -> None:
    """
    Generic ingestion engine to fetch weather data for multiple locations.

    Args:
        coordinates_path (Path): Path to CSV containing city coordinates.
        output_path (Path): Path where the raw JSON response will be saved.
        config (APIConfig): Configuration for the API request.
        retry_strategy (RetryStrategy): Strategy for API request retries.
        start_date (str, optional): Override start date (YYYY-MM-DD).
        end_date (str, optional): Override end date (YYYY-MM-DD).
        days (int, optional): Override number of days to fetch.
    """
    # 1. Load coordinates
    coordinates_df = pd.read_csv(coordinates_path)
    latitudes = join_column_text(coordinates_df["latitude"])
    longitudes = join_column_text(coordinates_df["longitude"])
    cities = coordinates_df["city"]

    # 2. Resolve parameters (Override OR Config)
    # CLI Overrides take priority over the base Config
    s_date = start_date or config.start_date
    e_date = end_date or config.end_date
    d_val = days or config.days

    # 3. Build API parameters
    params = {
        "latitude": latitudes,
        "longitude": longitudes,
        "hourly": config.hourly_vars,
    }
    
    if s_date:
        params["start_date"] = s_date
    if e_date:
        params["end_date"] = e_date
    
    # Only use 'forecast_days' if start/end dates are NOT provided
    # Open-Meteo ignores 'forecast_days' if dates are present
    if d_val and not (s_date or e_date):
        params["forecast_days"] = d_val

    # 4. Request API
    response = request_api(
        url=config.url, 
        endpoint=config.endpoint, 
        retry_strategy_obj=retry_strategy,
        **params
    )

    # 5. Enrich data with city names
    # Ensure response is a list (batch requests return a list)
    if not isinstance(response, list):
        response = [response]

    for i, city in enumerate(cities):
        response[i]["city"] = city

    # 6. Save raw data
    save_json(data=response, output_path=output_path)
