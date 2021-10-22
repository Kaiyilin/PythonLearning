"""helps you run code in parallel 
and speed up your code

Process
A Process is an instance of a program, e.g. a Python interpreter. 
They are independent from each other and do not share the same memory.

A process can have multiple threads inside 

Key facts:

Pros:
• A new process is started independently from the first process
• Takes advantage of multiple CPUs and cores
• Separate memory space --> Memory is not shared between processes
• One GIL (Global interpreter lock) for each process, i.e. avoids GIL limitation
• Great for CPU-bound processing
• Child processes are interruptable/killable

Cons:
• Starting a process is slower that starting a thread
• Larger memory footprint
• IPC (inter-process communication) is more complicated


Threads:
A thread is an entity within a process that can be scheduled for execution (Also known as "leightweight process"). 
A Process can spawn multiple threads. The main difference is that all threads within a process share the same memory.

Key facts:

• Multiple threads can be spawned within one process
• Memory is shared between all threads
• Starting a thread is faster than starting a process
• Great for I/O-bound tasks
• Leightweight - low memory footprint

Cons:
• One GIL for all threads, i.e. threads are limited by GIL
• Multithreading has no effect for CPU-bound tasks due to the GIL
• Not interruptible/killable -> be careful with memory leaks
• increased potential for race conditions (the condition where 2 or more threads want to modify the same variable at the same time)


Global Interpreter Lock (GIL)
A lock that allows onlt one thread at a time to execute in Python. 
This means that the GIL allows only one thread to execute at a time even in a multi-threaded architecture.

Why GIL is needed?
Needed in cPython because memory management is not thread-safe

How to avoid GIL? 
• Use multiprocessing 
• Use a different, free-threaded Python implementation (Jython, IronPython)
• Use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy
"""

