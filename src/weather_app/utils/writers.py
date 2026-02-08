import json
from pathlib import Path
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

def save_json(data:dict, output_path:Path)->None:
    """Saves data to output_path as json.

    Args:
        data (dict): Dictionary data
        output_path (Path): Path to writing destination
    """    

    # Creating parent folder for file if it does not exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write data to json file
    with open(output_path, "w") as json_file:
        json.dump(data, json_file)


def save_parquet(data:pd.DataFrame, output_path:Path, schema:pa.Schema)->None:
    """Saves data to output path as parquet. In enforces the schema.

    Args:
        data (pd.DataFrame): Data to be saved
        output_path (Path): Path to output
        schema (pa.Schema): Schema to be enforced
    """    

    # Creating parent folder for file if it does not exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Reading pd.DataFrame as a pyarrow table and writing to transformed data path
    table = pa.Table.from_pandas(data, schema=schema)
    pq.write_table(table=table, where=output_path)