import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')


def num_shutdowns(logfile):
    """
    Count and return the number of shutdowns present in the logfile.

    Args:
        logfile (str): The path to the logfile.

    Returns:
        int: The number of shutdowns present in the file. Note: a single shutdown event will have two entries:
        "Shutdown initiated" and "Shutdown complete".
    """
    shutdown_events = get_shutdown_events(logfile)
    return len(shutdown_events) // 2



# The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')
    


# The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')
    
