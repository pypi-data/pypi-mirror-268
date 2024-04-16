import time
import functools

def log_time(func):
    """Decorator to log the execution time of a function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Capture the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Capture the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result

    return wrapper

