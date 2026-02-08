import json
from pathlib import Path
import pandas as pd
# Project scripts, pathes and env variables
from weather_app.utils.request_api import request_api
from weather_app.configs import  RAW_DATA_DIR, COORDINATES_PATH, FORECAST_URL, FORECASTS_ENDPOINT, FORECAST_DAYS, HOURLY_VARIABLES
from weather_app.utils.wrangling import join_column_text

# Fetch data from each location
def fetch_forecasts(
        input_path: Path, 
        output_dir: Path
        ) ->None: 
    """
    Fetches forecasts data from the Open Weather api
    """

    # Reading coordinates and extracting necessary variables
    coordinates_df = pd.read_csv(input_path)
    latitudes = join_column_text(coordinates_df["latitude"])
    longitudes = join_column_text(coordinates_df["longitude"])
    cities=coordinates_df["city"]


    # Iterate over coordinate files to get data for requesting the open meteo api.
    response = request_api(
            url=FORECAST_URL, endpoint=FORECASTS_ENDPOINT, latitude=latitudes, 
            longitude=longitudes, hourly=HOURLY_VARIABLES, forecast_days=FORECAST_DAYS
        )
    
    # Writing city names to each item in the list of api responses
    for i, city in enumerate(cities):
        response[i]["city"]=city

    # Creating folder if it does not exist
    output_dir.mkdir(exist_ok=True)

    # Creating the file path
    file_path = output_dir / "forecasts.json"

    # # Write data to json file
    with open(file_path, "w") as json_file:
        json.dump(response, json_file)

if __name__ == '__main__':
    fetch_forecasts(input_path=COORDINATES_PATH, output_dir=RAW_DATA_DIR)