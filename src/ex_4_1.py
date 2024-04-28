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
    Counts the number of complete shutdown events in the log file.
    
    Args:
        logfile (str): The path to the log file.
        
    Returns:
        int: The number of complete shutdown events in the log file.
    """
    shutdown_events = get_shutdown_events(logfile)
    # Assuming each "Shutdown initiated" is paired with a "Shutdown complete"
    return len(shutdown_events) // 2


# The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')