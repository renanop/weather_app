import json

# Project scripts and pathes
from weather_app.utils.request_weather_api import request_weather_api
from weather_app.configs import  RAW_FORECASTS_DIR, COORDINATES_PATH, FORECAST_URL, FORECASTS_ENDPOINT, FORECAST_DAYS, HOURLY_VARIABLES


# Opening coordinates file
with open(COORDINATES_PATH) as f:
    coordinates = json.load(f)
    print(coordinates)


# Importing env variables

# Fetch data from each location
def fetch_forecasts():
    """
    Fetches forecasts data from the Open Weather api
    """
    for location in coordinates.keys():
        latitude = coordinates[location].get("latitude")
        longitude = coordinates[location].get("longitude")   
        response = request_weather_api(
            url=FORECAST_URL, endpoint=FORECASTS_ENDPOINT, latitude=latitude, 
            longitude=longitude, hourly=HOURLY_VARIABLES, forecast_days=FORECAST_DAYS
            )

        # Preparing folder for writing json file
        data_folder = RAW_FORECASTS_DIR

        # Creating folder if it does not exist
        data_folder.mkdir(exist_ok=True)

        # Creating the file path
        file_path = data_folder / f"{location.lower()}.json"

        # Write data to json file
        with open(file_path, "w") as json_file:
            json.dump(response, json_file)

if __name__ == '__main__':
    fetch_forecasts()