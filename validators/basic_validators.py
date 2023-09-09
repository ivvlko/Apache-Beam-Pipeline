"""
This module validates the data once we've read the csv
and casted it into a python dictionary
"""

def dummy_validator(row):
    """
    Dummy validator as example;
    """
    if row.get("partner") == "Grand Royale Casino":
        return {}
    return row