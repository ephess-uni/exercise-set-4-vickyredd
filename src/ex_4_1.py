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

    shutdown_count = 0
    i = 0
    while i < len(lines):
        if "Shutdown initiated" in lines[i]:
            # Look for corresponding "Shutdown complete" event
            j = i + 1
            while j < len(lines):
                if "Shutdown complete" in lines[j]:
                    shutdown_count += 1
                    i = j + 1  # Move i to the line after "Shutdown complete"
                    break
                j += 1
            else:
                # If no "Shutdown complete" event is found, move to the next line
                i += 1
        else:
            i += 1

    return shutdown_count



# The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')
    
