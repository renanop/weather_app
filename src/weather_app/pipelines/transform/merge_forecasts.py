import pandas as pd
from pathlib import Path
import json 
from weather_app.configs import RAW_FORECASTS_DIR, TRANSFORMED_DATA_DIR

# Defining pathes
forecasts_filename = "forecasts.parquet"
full_writing_path = TRANSFORMED_DATA_DIR / forecasts_filename 

# Fetching json files pathes
files = Path.glob(RAW_FORECASTS_DIR, "*.json")

def merge_forecasts():
# Reading data in each json file
    df_list = []
    for f in files:
        with open(f, "r") as json_file:
            temperatures = json.load(json_file)

        # Fetching time and temperature data
        data = temperatures["hourly"]

        # Reading data as dataframe
        df = pd.DataFrame(data)

        # Including city names
        df["city"] = f.stem

        # Adding df to the df list
        df_list.append(df)

    # Merging dataframes
    weathers_df = pd.concat(df_list, ignore_index=True)

    # Converting dates to datetime format
    weathers_df["time"] = pd.to_datetime(weathers_df["time"], format="%Y-%m-%dT%H:%M")

    # Writing data
    weathers_df.to_parquet(full_writing_path)


if __name__=="__main__":
    merge_forecasts()


