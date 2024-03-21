#!/usr/bin/env python3
'''Software for managing and tracking environmental data from field project.'''
import argparse
from catchment import models, views

def main(args):
    '''The MVC Controller of the environmental data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    '''

    in_files = args.infiles
    if not isinstance(in_files, list):
        in_files = [args.infiles]

    for filename in in_files:
        measurement_data = models.read_variable_from_csv(filename, args.measurements)

        view_data = {
            'daily sum': models.daily_total(measurement_data),
            'daily average': models.daily_mean(measurement_data),
            'daily max': models.daily_max(measurement_data),
            'daily min': models.daily_min(measurement_data)
        }

        views.visualize(view_data)

def create_argparse():
    parser = argparse.ArgumentParser(
    description='A basic environmental data management system')

    req_group = parser.add_argument_group('required arguments')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing measurement data')

    req_group.add_argument(
        '-m', '--measurements',
        help='The name of the measurement data series to load',
    )

    parser.add_argument('--full-data-analysis',
                        action='store_true',
                        dest='full_data_analysis')
    return parser

if __name__ == "__main__":
    parser = create_argparse()
    args = parser.parse_args()

    main(args)
