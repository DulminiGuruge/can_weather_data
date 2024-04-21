# Canada Weather Data Package

**can_weather_data** is a Python library that allows you to retrieve weather data from climate.weather.gc.ca. This package provides functions to extract historical weather data for a given location and time period. It uses the **env_canada** library to access historical weather data from Environment and Climate Change Canada.

### Installation

pip install can_weather_data

### Usage

```python
from can_weather_data.weatherdata import data_extract

cord_list = ['48.508333', '-68.467667']

# Set the start and end dates for the weather data retrieval.
start_date = datetime.strptime('Jan2015', '%b%Y')
end_date = datetime.strptime('Dec2020', '%b%Y')

data_extract(cord_list, start_date, end_date)
```





