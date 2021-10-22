import functools

def starter_deco(func):
    
    @functools.wraps(func) # this decorator allows you to preserve the info of func you use
    def wrapper(*args, **kwargs): # allows you to use as many args and kwargs as you want
        print("start")
        result = func(*args, **kwargs) # again, you need to allow the function use args and kwargs
        return result # allow you to obtain the result of the func otherwise it's None
    return wrapper

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

# if you uses more than one decorator, 
# it'll use in the order you stack it 

@starter_deco # excute this
@repeat(num_times=4) # inside the starter_deco function, it'll excute repeat function
def say_sthg(sthg):
    say_sthg = "{}".format(sthg)
    print(say_sthg)
    return say_sthg

say_sthg("Json") # inside the repeat function, it'll use say hello function


# the value of nested decorator is like you can call for a debugger, 
# and let execute first 

def debugger_deco(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}") # with !r inside the fstring, will add quotation mark 
        return result
    return wrapper

@debugger_deco
@starter_deco
@repeat(num_times=5)
def say_sthg(sthg):
    say_sthg = "{}".format(sthg)
    print(say_sthg)
    return say_sthg
say_sthg("Json")