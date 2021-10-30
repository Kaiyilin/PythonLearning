import threading
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

def testThread(num):
    print(num)

@time_decorator
def main():
    for i in range(5000000):
        t = threading.Thread(target=testThread, args=(i,))
        t.start()

if __name__ == '__main__':
    main()