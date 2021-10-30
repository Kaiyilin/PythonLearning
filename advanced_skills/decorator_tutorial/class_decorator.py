"""basically does the same thing to function decorators
but typically used if we want to maintain and update a state.
"""
class CountCalls:
    def __init__(self, func) -> None:
        self.func = func
        self.numcalls = 0
    
    # __call methods allows you to execute a obj of this class just like function
    def __call__(self, *args, **kwargs): 
        # print("Hi there")
        self.numcalls += 1
        print(f"Execution {self.numcalls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello")