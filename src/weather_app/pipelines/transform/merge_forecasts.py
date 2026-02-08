import pandas as pd
from pathlib import Path
import json 
from weather_app.configs import RAW_FORECASTS_PATH, TRANSFORMED_FORECASTS_PATH
import pyarrow as pa
import pyarrow.parquet as pq



def forecasts_to_parquet(
        input_path:Path, 
        output_path:Path
        ):
    """
    Reads raw forecasts json data and transforms it into a parquet table with enforced schema
    
    :param input_path: Description
    :param output_path: Description
    :return: Description
    :rtype: NoReturn
    """

    # Reading input data
    with open(input_path, "r") as file:
        f = json.load(file)
    
    # Iterate over list of api responses and populate a new list of pd.DataFrames
    lst=[]
    for item in f:
        df = pd.DataFrame()
        # Grab each weather variable and its contents and transform them into pd.DataFrame columns.
        for k, v in f[0]["hourly"].items():
            df[k] = v
        df["city"] = item["city"]
        lst.append(df)

    # Concatenate all pd.DataFrames to get the final df.
    df = pd.concat(lst)

   # Converting dates to datetime format and enforcing schema
    df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%dT%H:%M")


    # Enforcing schema
    schema = pa.schema([
    ('time', pa.timestamp('us')),
    ('city', pa.string()),
    ('temperature_2m', pa.float64()),
    ('precipitation_probability', pa.float64()),
    ('precipitation', pa.float64()),
    ])
    
    # Reading pd.DataFrame as a pyarrow table and writing to transformed data path
    table = pa.Table.from_pandas(df, schema=schema)
    pq.write_table(table=table, where=output_path)

if __name__=="__main__":
    forecasts_to_parquet(input_path=RAW_FORECASTS_PATH, output_path=TRANSFORMED_FORECASTS_PATH)


