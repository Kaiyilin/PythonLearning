from threading import Thread
import os 

def sqr_nums():
    for i in range(100000):
        print(i * i)

if __name__ == "__main__":

    threads = []
    num_threads = 10 #  self-defined
    # create processes
    for i in range(num_threads):
        thread = Thread(target=sqr_nums)
        threads.append(thread)
    
    # start all process 
    for thread in threads:
        thread.start()
    
    # wait for all processes to finish
    # block the main thread until these processes are finished
    for thread in threads:
        thread.join()