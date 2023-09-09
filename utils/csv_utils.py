"""
This module provides basic csv utils
"""

import csv
import io


from mappings.csv_files import CSV_MAPPING_COLUMNS


def parse_csv(row, type_of_data="partners_data"):
    """
    Parse row from csv file and is invoked in apache beam pipeline;

        Parameters:
            row (str): raw text value from csv doc;
            type_of_data (str): the type of csv files we will process. Default partners_data
        
        Returns:
            row_dict(dict): the processed row in dictionary format
    """

    row_io = io.StringIO(row, newline='')
    csv_reader = csv.reader(row_io, delimiter=',', skipinitialspace=True)

    column_names = next(csv_reader)
    row_dict = {col: value.strip() for col, value in zip(column_names, next(csv_reader))}
    numeric_columns = CSV_MAPPING_COLUMNS.get(type_of_data).get("numeric_columns")

    return {col: float(value) if col in numeric_columns else value for col, value in row_dict.items()}

