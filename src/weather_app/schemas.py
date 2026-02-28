from dataclasses import dataclass
from typing import Optional
import pyarrow as pa

# dataclass for open meteo request api config
@dataclass(frozen=True)  # frozen=True -> imutable
class APIConfig:
    """
    Configuration object for managing Open-Meteo API request parameters.

    Attributes:
        url (str): The base URL for the API (e.g., "https://api.open-meteo.com/").
        endpoint (str): The specific service endpoint (e.g., "/v1/forecast/").
        hourly_vars (str): Comma-separated list of weather variables to fetch.
        start_date (str, optional): The beginning of the period (YYYY-MM-DD).
        end_date (str, optional): The end of the period (YYYY-MM-DD).
        days (int, optional): Number of days to fetch (legacy/interactive use).
    """
    url: str
    endpoint: str
    hourly_vars: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    days: Optional[int] = None

@dataclass(frozen=True)  # frozen=True -> imutable
class RetryStrategy:
    """Data class to config the Retry object from urllib3"""
    total_retries: int
    backoff_factor: float
    status_forcelist: list
    allowed_methods: list

# Forecasts table schema
FORECASTS_TABLE_SCHEMA = pa.schema([
('time', pa.timestamp('us')),
('city', pa.string()),
('temperature_2m', pa.float64()),
('precipitation_probability', pa.float64()),
('precipitation', pa.float64()),
])
