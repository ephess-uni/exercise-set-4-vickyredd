""" ex_4_2.py """
from datetime import datetime

def logstamp_to_datetime(datestr):
    """
    Converts a log timestamp string to a datetime.datetime object.
    
    Args:
        datestr (str): The log timestamp string in the format "YYYY-MM-DDTHH:MM:SS".
        
    Returns:
        datetime.datetime: The datetime object corresponding to the input timestamp.
    """
    return datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')


# The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')