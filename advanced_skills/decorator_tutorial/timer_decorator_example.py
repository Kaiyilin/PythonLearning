import time
import functools

def time_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time() # in sec
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_mins = (end_time - start_time) / 60
        print(f"Overall execution time of {func.__name__} function is {exec_mins} mins")
        return result
    
    return wrapper

@time_decorator
def main():
    for _ in range(60000):
        print("hi")

main()