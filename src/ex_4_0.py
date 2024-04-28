try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')


def get_shutdown_events(logfile):
    """
    Reads the log file and returns a list of lines where a shutdown was initiated.
    
    Args:
        logfile (str): The path to the log file.
        
    Returns:
        list: A list of lines where a shutdown was initiated.
    """
    shutdown_events = []
    
    try:
        with open(logfile, 'r') as file:
            for line in file:
                if 'Shutdown initiated' in line:
                    shutdown_events.append(line.strip())
    except FileNotFoundError:
        print(f"Error: {logfile} not found.")
        return []
    
    return shutdown_events


# The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")