import pandas as pd
from pathlib import Path
from weather_app.configs import RAW_FORECASTS_PATH, TRANSFORMED_FORECASTS_PATH
import pyarrow as pa
from weather_app.schemas import FORECASTS_TABLE_SCHEMA
from weather_app.utils.writers import save_parquet
from weather_app.utils.readers import read_json


def transform_forecasts(
        data:dict, 
        ):
    """Apply transformations to the forecasts data.
    1. Transforms forecast json data, selecting hourly variables and city and converts everything to a pd.DataFrame.
    2. Converts time column from string to datetime.

    Args:
        data (dict): Forecasts dictionary

    Returns:
        df (pd.DataFrame): Forecasts pd.DataFrame
    """
    
    # Iterate over list of api responses and populate a new list of pd.DataFrames
    df_list=[]
    for item in data:
        df = pd.DataFrame()

        # Grab each weather variable and its contents and transform them into pd.DataFrame columns.
        for k, v in data[0]["hourly"].items():
            df[k] = v
        df["city"] = item["city"]
        df_list.append(df)

    # Concatenate all pd.DataFrames to get the final df.
    df = pd.concat(df_list)

   # Converting dates to datetime format and enforcing schema
    df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%dT%H:%M")

    return df


def run_transform_forecasts_pipeline(input_path: Path, output_path:Path, schema:pa.Schema)->None:
    """Encapsulates transformation pipeline logic

    Args:
        input_path (Path): path to input data
        output_path (Path): path to writing destination
        schema (pa.Schema): schema to be enforced on transformed data
    """
    # Reads input data
    data = read_json(input_path=input_path)

    # Runs transformations
    df = transform_forecasts(data=data)

    # Writes to destination path enforcing schema
    save_parquet(data=df, output_path=output_path, schema=schema)


if __name__=="__main__":
    run_transform_forecasts_pipeline(
        input_path=RAW_FORECASTS_PATH, 
        output_path=TRANSFORMED_FORECASTS_PATH,
        schema=FORECASTS_TABLE_SCHEMA
        )


