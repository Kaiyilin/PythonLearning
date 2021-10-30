import os 
from multiprocessing import Process

def sqr_nums():
    for i in range(100000):
        print(i * i)

if __name__ == "__main__":

    processes = []
    num_processes = os.cpu_count()
    # create processes
    for i in range(num_processes):
        p = Process(target=sqr_nums) # if the target function itself has args, you can specify in args argument
        processes.append(p)
    
    # start all process 
    for process in processes:
        process.start()
    
    # wait for all processes to finish
    # block the main thread until these processes are finished
    for process in processes:
        process.join()