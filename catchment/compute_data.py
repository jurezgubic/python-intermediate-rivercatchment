"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views

class CSVDataSource:
    def __init__(self, dir_path):
        self.dir_path = dir_path
    def load_catchment_data(self):
        """Function to read in all csvs from data directory"""
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'rain_data_2015*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError('No CSV files found in the data directory')
        data = map(models.read_variable_from_csv, data_file_paths)
        return data 
    
class JSONDataSource:
    def __init__(self, dir_path):
        self.dir_path = dir_path
    def load_catchment_data(self):
        """Function to read in all jsons from data directory"""
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'rain_data_2015*.json'))
        if len(data_file_paths) == 0:
            raise ValueError('No CSV files found in the data directory')
        data = map(models.read_variable_from_json, data_file_paths)
        return data 


def compute_standard_deviation_by_day(data):
    """Function to calculate standard deviation for daily data"""
    daily_std_list = list(map(models.daily_std, data))
    daily_standard_deviation = pd.concat(daily_std_list)
    return daily_standard_deviation

def analyse_data(data_source):
    """Calculate the standard deviation by day between datasets"""
    data = data_source.load_catchment_data()
    return compute_standard_deviation_by_day(data)
