import json
from pathlib import Path
import requests
from requests.adapters import HTTPAdapter  
from urllib3.util.retry import Retry
from weather_app.schemas import RetryStrategy

def request_api(
        url:str, 
        endpoint:str, 
        retry_strategy_obj:RetryStrategy, 
        **kwargs
        )-> dict:
    """
    Make a request on the Weather Forecast API. Use args as request params
    
    :param args: Parameters for the request on the Weather Forecast API
    """
    # Building full url
    full_url = url + endpoint

    # Getting query parameters
    params=kwargs

    # Unpacking retry strategy in the Retry object
    retry_strategy = Retry(
        total=retry_strategy_obj.total_retries,
        backoff_factor=retry_strategy_obj.backoff_factor,
        status_forcelist=retry_strategy_obj.status_forcelist,
        allowed_methods=retry_strategy_obj.allowed_methods
    )

    # Attach the retry strategy to an HTTPAdapter  
    adapter = HTTPAdapter(max_retries=retry_strategy)  
    session = requests.Session()  
    session.mount("https://", adapter)  
    session.mount("http://", adapter)  

    # Making Request
    response = session.get(url = full_url, params=params)
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