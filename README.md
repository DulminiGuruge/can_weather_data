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



#### The directory structure of the package.:

```python
 can_weather_data/
│
├── can_weather_data/
│   ├── __init__.py
│   └── weatherdata.py
│
├── README.md
├── LICENSE
└── setup.py
```

1. can_weather_data/: The root directory of the package.
2. can_weather_data/can_weather_data/: The Python package directory.
3. can_weather_data/can_weather_data/__init__.py: Initialization script.
4. can_weather_data/can_weather_data/weatherdata.py: Python module containing the function.
5. README.md: Description of the package.
6. LICENSE: License for the package.
7. setup.py: Script to package the project.

#### Build and Install the Package

##### Build the package

>cd weather_package

>python setup.py sdist bdist_wheel

##### Install the package

>pip install .

