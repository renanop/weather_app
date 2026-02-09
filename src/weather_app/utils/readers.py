import json
from pathlib import Path
import requests

def request_api(url, endpoint, **kwargs):
    """
    Make a request on the Weather Forecast API. Use args as request params
    
    :param args: Parameters for the request on the Weather Forecast API
    """
    full_url = url + endpoint
    params=kwargs

    # Making Request
    response=requests.get(url = full_url, params=params)
    response = response.json()

    return response


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