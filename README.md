## Let's convert the provided weatherdata.py file into a Python package. Here are the steps:

### Step 1: Organize your files

Create a directory structure for your package. A typical structure would look something like this:


```python
 weather_package/
│
├── weather_package/
│   ├── __init__.py
│   └── weatherdata.py
│
├── README.md
├── LICENSE
└── setup.py
```


1. weather_package/: The root directory of the package.
2. weather_package/weather_package/: The Python package directory.
3. weather_package/weather_package/__init__.py: Initialization script.
4. weather_package/weather_package/weatherdata.py: Python module containing the function.
5. README.md: Description of the package.
6. LICENSE: License for the package.
7. setup.py: Script to package the project.

# Canada Weather Data Package

A Python package to retrieve weather data from climate.weather.gc.ca.

### Installation

pip install weather_package

### Usage

```python
from weather_package.weatherdata import data_extract

cord_list = ['48.508333', '-68.467667']

# Set the start and end dates for the weather data retrieval.
start_date = datetime.strptime('Jan2015', '%b%Y')
end_date = datetime.strptime('Dec2020', '%b%Y')

data_extract(cord_list, start_date, end_date)