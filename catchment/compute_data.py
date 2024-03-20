"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views

class CSVDataSource:
  """
  Loads all the catchment CSV files within a specified directory.
  """
  def __init__(self, dir_path):
    self.dir_path = dir_path

  # New function reads the data in format needed
  def load_catchment_data(self):
    data_file_paths = glob.glob(os.path.join(self.dir_path, 'rain_data_2015*.csv'))
    if len(data_file_paths) == 0:
      raise ValueError('No CSV files found in the data directory')
    data = map(models.read_variable_from_csv, data_file_paths)
    return list(data)
  

class JSONDataSource:
    """
    Loads patient data with catchment values from JSON files within a specified folder.
    """
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_catchment_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'rain_data_2015*.json'))
        if len(data_file_paths) == 0:
            raise ValueError('No JSON files found in the data directory')
        data = map(models.read_variable_from_json, data_file_paths)
        return list(data)

# Calculate the standard deviation by day between datasets.
def compute_standard_deviation_by_day(data):
   daily_std_list = map(daily_std, data)

   daily_standard_deviation = pd.concat(daily_std_list)
   return daily_standard_deviation

# function, daily_std, to calculate the standard deviation by day for any dataframe
def daily_std(data):
    return data.groupby(data.index.date).std()

# Gets all the measurement data from the CSV files in the data directory,
# then graphs the standard deviation


def analyse_data(data_source):
  data = data_source.load_catchment_data()
  daily_standard_deviation = compute_standard_deviation_by_day(data)

  return daily_standard_deviation

