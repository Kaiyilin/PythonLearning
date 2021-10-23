"""Context managers are a great tool for resource management. 
They allow you to allocate and release resources precisely when you want to. 
A well-known example is the with open() statemtent:

mode
“ r “, for reading.
“ w “, for writing.
“ a “, for appending.
“ r+ “, for both reading and writing

Examples of context managers
Open and close files
open and close database connections [VVV]
Acquire and release locks:
"""

with open("note.txt", "w+") as file:
    file.write("Hello world")

# if not using with statement, the typical way 
file = open("note.txt", "r+")
try: 
    file.write("Hello world")
    file.write("Hello world")
finally: # close the file
    file.close()

# Advanced way for context manage 
class ManageFile():
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def __enter__(self):
        """enter method
        will be executed as soon as we enter the with statement
        where we allocate our resources
        """
        print("enter")
        self.file = open(self.file_name, "w")
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        """exit method
        exc_type: exception type 
        exc_val: exception value
        exc_tb: exception traceback

        we need to make sure we correctly close our file
        """
        if self.file:
            self.file.close()
        
        # handle the exception, otherwise you won't be able to deal
        # with further code
        if exc_type is not None:
            print('handle exception') 
        print(f"Exit {self.file_name}")
        return True # Ehy return True??


with ManageFile('note.txt') as file: # first to __init__method
    file.write("Hello") # as long as we're in with statement, we use __enter__ method
    file.unexitmethod() # raise the exception
 
# __exit__ here 

"""Instead of writing a class, 
we can also write a generator function and decorate it 
with the contextlib.contextmanager decorator. 
Then we can also call the function using a with statement. 
For this approach, the function must yield the resource in a try statement, 
and all the content of the __exit__ method to free up 
the resource goes now inside the corresponding finally statement.
"""
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()
        
with open_managed_file('notes.txt') as f:
    f.write('some todo...')


# Bonaus: Real example for database connection, the Mongo connection
from pymongo import MongoClient

class MongoDBConnection(object):
    """MongoDB Connection"""
    def __init__(self, host='localhost', port='27017'):
        self.host = host
        self.port = port
        self.connection = None
    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

mongo = MongoDBConnection()
with mongo:
    collection = mongo.connection.MyDbName.Customers
    customer = collection.find({'_id': 123})
    print(customer.get('name'))