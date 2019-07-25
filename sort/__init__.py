import time
from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('{}: {}'.format(func.__name__, end_time-start_time))
    return wrapper