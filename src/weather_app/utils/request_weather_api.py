import requests

def request_weather_api(url, endpoint, **kwargs):
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





