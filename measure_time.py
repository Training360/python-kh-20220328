from datetime import datetime
import time


def time_decorator(function):
    def wrapper(*args):
        start = datetime.now()
        result = function(*args)
        end = datetime.now()
        print(end - start)
        return result        
    return wrapper

@time_decorator
def dummy(name):
    time.sleep(2)
    print(name)

dummy("John Doe")