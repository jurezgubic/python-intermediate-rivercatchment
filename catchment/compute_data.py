"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views


def analyse_data(data_dir):
    """Analyse the data in the data directory."""
    data = load_data(data_dir)
    daily_standard_deviation = compute_standard_deviation_by_day(data)
    return daily_standard_deviation


def load_data(data_dir):
    """Load all the data from the CSV files in the data directory."""
    data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError('No CSV files found in the data directory')
    data = map(models.read_variable_from_csv, data_file_paths)
    return data


def compute_standard_deviation_by_day(data):
    daily_std_list = map(models.daily_std, data)

    daily_standard_deviation = pd.concat(daily_std_list)
    return daily_standard_deviation
