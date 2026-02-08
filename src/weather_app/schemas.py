from dataclasses import dataclass
import pyarrow as pa

# dataclass for open meteo request api config
@dataclass(frozen=True)  # frozen=True -> imutable
class APIConfig:
    url: str
    endpoint: str
    days: int
    hourly_vars: str


# Forecasts table schema
FORECASTS_TABLE_SCHEMA = pa.schema([
('time', pa.timestamp('us')),
('city', pa.string()),
('temperature_2m', pa.float64()),
('precipitation_probability', pa.float64()),
('precipitation', pa.float64()),
])
