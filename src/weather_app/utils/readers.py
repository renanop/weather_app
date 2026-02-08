import json
from pathlib import Path

def read_json(input_path: Path)->dict:
    """Reads a json file

    Args:
        input_path (Path): Path to json file

    Returns:
        dict: Dictionary obtained from the json file
    """    
    with open(input_path, "r") as file:
        f = json.load(file)

    return f