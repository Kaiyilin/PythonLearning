""" every advanced python user should know that
 2 types, function (more common) and class decorators

what decorators do is it takes another function as 
argument and extends the behaviour of this function without 
explicitly modify it, which allows you to add new functionality 
to an existing function 

The usage of decorator
e.g. a time decorator to record execution time, 
debug decorator, 
check decorator to check if the arguments fullfill some requirements 
"""

# without argument
def starter_deco(func):
    
    def wrapper():
        print("start")
        func()
    return wrapper

@starter_deco
def print_sthg():
    print("sthg")

#print_sthg = starter_deco(print_sthg)
print_sthg()

# with argument
def starter_deco(func):
    
    def wrapper(*args, **kwargs): # allows you to use as many args and kwargs as you want
        print("start")
        result = func(*args, **kwargs) # again, you need to allow the function use args and kwargs
        return result # allow you to obtain the result of the func otherwise it's None
    return wrapper

@starter_deco
def add_5(x):
    return x + 5

@starter_deco
def print_sthg():
    print("sthg")

# it works even the function requires no args
print_sthg()

r = add_5(255)
print(r)

"""Key concepts, the function identity

in case 1, the add_5 function will consider it as a wrapper function, instead of add_5 function
therfore, if you call __name__ and __doc__ it will return the name of wrapper and the docstr of wrapper

e.g.
print(add_5.__name__)
print(add_10.__name__)
print(add_5.__doc__)
print(add_10.__doc__)

Outputs:
wrapper
add_10
None
helps you add 10 to the nums


To fix it, where I import the functools.
By using another decorator before wrapper, 
it preserves the info of func you use

in case 2,

e.g.
print(add_5.__name__)
print(add_10.__name__)
print(add_5.__doc__)
print(add_10.__doc__)

Outputs:
add_5
add_10
helps you add 5 to the nums
helps you add 10 to the nums
"""
# case 1, python messed up with the function identity
def starter_deco(func):
    
    def wrapper(*args, **kwargs): # allows you to use as many args and kwargs as you want
        print("start")
        result = func(*args, **kwargs) # again, you need to allow the function use args and kwargs
        return result # allow you to obtain the result of the func otherwise it's None
    return wrapper

@starter_deco
def add_5(x):
    """helps you add 5 to the nums
    """
    return x + 5

def add_10(x):
    """helps you add 10 to the nums
    """
    return x + 10

print(add_5.__name__)
print(add_10.__name__)
print(add_5.__doc__)
print(add_10.__doc__)

# case 2, import functools
import functools

def starter_deco(func):
    
    @functools.wraps(func) # this decorator allows you to preserve the info of func you use
    def wrapper(*args, **kwargs): # allows you to use as many args and kwargs as you want
        print("start")
        result = func(*args, **kwargs) # again, you need to allow the function use args and kwargs
        return result # allow you to obtain the result of the func otherwise it's None
    return wrapper

@starter_deco
def add_5(x):
    """helps you add 5 to the nums
    """
    return x + 5

def add_10(x):
    """helps you add 10 to the nums
    """
    return x + 10

print(add_5.__name__)
print(add_10.__name__)
print(add_5.__doc__)
print(add_10.__doc__)

