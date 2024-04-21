
# Import packages
import pandas as pd
import numpy as np
from dateutil import rrule
import asyncio
from env_canada.ec_historical import get_historical_stations


def getData(stationID, year, month):
    """
    This function retrieves weather data for a given station, year, and month.

    Args:
        stationID (str): The ID of the weather station.
        year (int): The year for which to retrieve data.
        month (int): The month for which to retrieve data.

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the weather data.
    """
    base_url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?"
    query_url = "format=csv&stationID={}&Year={}&Month={}&timeframe=2".format(stationID, year, month)
    api_endpoint = base_url + query_url
    return pd.read_csv(api_endpoint, skiprows=0)

def getData_btween_dates(stationID, start_date, end_date):
    """
    This function retrieves weather data for a given station between two dates.

    Args:
        stationID (str): The ID of the weather station.
        start_date (datetime.date): The start date for the data retrieval.
        end_date (datetime.date): The end date for the data retrieval.

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the weather data.
    """
    frames = []
    for dt_i in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
        df = getData(stationID, dt_i.year, dt_i.month)
        frames.append(df)

    weather_data = pd.concat(frames)
    weather_data.reset_index(inplace=True)
    weather_data['Date/Time'] = [pd.to_datetime(weather_data['Date/Time'][i]).date() for i in range(len(weather_data))]

    return weather_data

def data_extract(coordinates,start,end):
    """
    This function extracts weather data for a given location and time period.

    Args:
      coordinates (tuple): A tuple containing the latitude and longitude of the location.
      start (datetime.date): The start date for the data retrieval.
      end (datetime.date): The end date for the data retrieval.

    Returns:
      pd.DataFrame: A Pandas DataFrame containing the weather annualized data.
    """

    stations = pd.DataFrame(asyncio.run(get_historical_stations(coordinates, start_year=start.year,
                                                    end_year=end.year, radius=50, limit=100))).T
    stations.reset_index(inplace=True)
    station_count = len(stations)
    if station_count==0:
      return pd.DataFrame(columns=['year', 'snow', 'rain', 'precip',
                                   'max_temp', 'min_temp', 'lat','long'])
    for i in range(station_count):
      station_id = stations['id'][i]
      df_temp =  getData_btween_dates(station_id, start, end )
      df_temp = df_temp[['Date/Time','Mean Temp (°C)', 'Total Snow (cm)', 'Total Precip (mm)', 'Total Rain (mm)',
                        'Max Temp (°C)', 'Min Temp (°C)' ]]
      df_temp.columns = [f'{i}_Date/Time', f'{i}_mean_temp', f'{i}_snow', f'{i}_precip', f'{i}_rain',
                        f'{i}_max_temp', f'{i}_min_temp']

      if i ==0:
        df = df_temp
      else:
        df = pd.concat([df,df_temp], axis=1)

    df_anual= pd.DataFrame()
    #print(df.columns)
    df_anual['date'] = df['0_Date/Time']
    col_list = ['mean_temp', 'snow', 'precip', 'rain', 'max_temp', 'min_temp']
    for col in col_list:
      df_anual[col] = np.mean(df[[f'{i}_{col}' for i in range(station_count)]], axis=1)

    df_anual['year'] = [df_anual.date[i].year
                        if df_anual.date[i].month<10
                        else df_anual.date[i].year+1
                        for i in range(len(df_anual))]
    df_final = pd.DataFrame()
    df_final['snow']= df_anual.groupby('year')['snow'].sum()
    df_final['rain']= df_anual.groupby('year')['rain'].sum()
    df_final['precip']= df_anual.groupby('year')['precip'].sum()
    df_final['max_temp']= df_anual.groupby('year')['max_temp'].max()
    df_final['min_temp']= df_anual.groupby('year')['min_temp'].min()
    df_final.reset_index(inplace=True)
    df_final['lat'] = np.full(len(df_final), coordinates[0])
    df_final['long'] = np.full(len(df_final), coordinates[1])
    return df_final