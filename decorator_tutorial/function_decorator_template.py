import functools

# templates
def my_decorator(func):
    
    @functools.wraps(func) # this decorator allows you to preserve the info of func you use
    def wrapper(*args, **kwargs): # allows you to use as many args and kwargs as you want
        # do sthg
        result = func(*args, **kwargs) # again, you need to allow the function use args and kwargs
        # do sthg
        return result # allow you to obtain the result of the func otherwise it's None
    return wrapper

# The decorator itself can also take arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    print("{}".format(name))

greet("Json")