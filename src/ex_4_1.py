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
    with open(logfile, 'r') as file:
        lines = file.readlines()

    count = 0
    i = 0
    while i < len(lines):
        if "Shutdown initiated" in lines[i] and i + 1 < len(lines) and "Shutdown complete" in lines[i + 1]:
            count += 1
            i += 2  # Skip to the next pair of shutdown lines
        else:
            i += 1

    return count


# The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')
    
