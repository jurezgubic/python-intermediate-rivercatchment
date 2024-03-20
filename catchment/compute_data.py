"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views

# New function reads the data in format needed
def load_catchment_data(dir_path):
  data_file_paths = glob.glob(os.path.join(dir_path, 'rain_data_2015*.csv'))
  if len(data_file_paths) == 0:
      raise ValueError('No CSV files found in the data directory')
  data = map(models.read_variable_from_csv, data_file_paths)
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
def analyse_data(data_dir):
  data = load_catchment_data(data_dir)
  daily_standard_deviation = compute_standard_deviation_by_day(data)

  graph_data = {
       'standard deviation by day': daily_standard_deviation,
   }
   # views.visualize(graph_data)
  return daily_standard_deviation

