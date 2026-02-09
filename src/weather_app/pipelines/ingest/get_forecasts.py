from pathlib import Path
import pandas as pd
# Project scripts, pathes and env variables
from weather_app.utils.readers import request_api
from weather_app.configs import  RAW_FORECASTS_PATH, COORDINATES_PATH, REQUEST_FORECASTS_CONFIG, RETRY_STRATEGY
from weather_app.utils.wrangling import join_column_text
from weather_app.utils.writers import save_json
from weather_app.schemas import APIConfig

# Fetch data from each location
def get_forecasts(
        input_path: Path,
        config: APIConfig 
        ) -> dict: 
    """ Get forecast data from API.

    Args:
        input_path (Path): Path to location coordinates data
        config (APIConfig): Config object with request parameters

    Returns:
        dict: response data
    """ 

    # Reading coordinates and extracting necessary variables
    coordinates_df = pd.read_csv(input_path)
    latitudes = join_column_text(coordinates_df["latitude"])
    longitudes = join_column_text(coordinates_df["longitude"])
    cities=coordinates_df["city"]


    # Requests forecasts data from the api
    response = request_api(
            url=config.url, endpoint=config.endpoint, retry_strategy_obj=RETRY_STRATEGY,
            latitude=latitudes, longitude=longitudes, hourly=config.hourly_vars, 
            forecast_days=config.days
        )
    
    # Writing city names to each item in the list of api responses
    for i, city in enumerate(cities):
        response[i]["city"]=city

    return response



def run_get_forecasts_pipeline(input_path:Path, output_path:Path, config: APIConfig)->None:
    """Encapsulates get forecast pipeline logic

    Args:
        input_path (Path): input path to location coordinate data
        output_path (Path): writing path to response data
    """    

    # get forecast data
    response = get_forecasts(input_path=input_path, config=config)

    # write data to output path
    save_json(data=response, output_path=output_path)



if __name__ == '__main__':
    run_get_forecasts_pipeline(input_path=COORDINATES_PATH, output_path=RAW_FORECASTS_PATH, config=REQUEST_FORECASTS_CONFIG)