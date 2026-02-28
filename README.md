# Weather App Data Pipeline

A modular ETL (Extract, Transform, Load) pipeline for fetching and processing weather forecasts from the [Open-Meteo API](https://open-meteo.com/).

## Project Overview

This project automates the ingestion of weather data for specific geographic locations and transforms it into a structured, high-performance Parquet format. It is designed for scalability and data integrity, using `pyarrow` schemas and robust retry logic.

### Architecture
- **Ingestion Engine (`engine.py`)**: A generic weather data extractor that handles coordinate-based API requests and city-name enrichment.
- **Forecast Pipeline (`get-forecasts`)**: Fetches 14-day forecasts for the configured cities and saves to `data/raw/forecasts.json`.
- **Actuals Pipeline (`get-actuals`)**: Fetches historical weather records from the archive API and saves to `data/raw/actuals.json`.
- **Transform Pipeline (`transform-forecasts`)**: Reads raw JSON, flattens structures into a `pandas` DataFrame, and saves as Parquet.
- **Data Integrity**: Enforces a strict schema (defined in `schemas.py`) during the transformation stage to ensure downstream consistency.

## Getting Started

### Prerequisites
- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (Extremely fast Python package manager)

### Installation
Clone the repository and sync the environment:
```bash
uv sync
```

## Running the Pipelines

The project uses `uv` to manage environment-safe execution.

### 1. Ingest Forecasts
Fetches the latest forecasts (default 14 days) for the configured cities.
```bash
uv run get-forecasts
```
**Options:**
- `--start-date`: Start date in `YYYY-MM-DD` format.
- `--end-date`: End date in `YYYY-MM-DD` format.
- `--days`: Number of forecast days to fetch.

### 2. Ingest Actuals (Historical Data)
Fetches historical records from the Open-Meteo archive.
```bash
uv run get-actuals --start-date 2026-01-01 --end-date 2026-01-01
```

### 3. Transform Data
Processes the raw forecasts into structured Parquet files.
```bash
uv run transform-forecasts
```

## Configuration

- **Coordinates**: Add or remove cities in `configs/coordinates.csv`.
- **API Settings**: Modify variables like `forecast_days` or `hourly_vars` in `src/weather_app/configs.py`.

## Data Schema

The transformed data is stored with the following schema:
- `time`: Timestamp (Microseconds)
- `city`: String
- `temperature_2m`: Float64
- `precipitation_probability`: Float64
- `precipitation`: Float64

## Development

### Linting and Formatting
The project uses `ruff` for maintaining code quality.
```bash
uv run ruff check .
```

### Testing
Run the test suite (currently under development):
```bash
uv run pytest
```
