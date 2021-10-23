"""Outline
• The difference between arguments and parameters
• Positional and keyword arguments
• Default arguments
• Variable-length arguments (*args and **kwargs)
• Container unpacking into function arguments
• Local vs. global arguments
• Parameter passing (by value or by reference?)
"""

# 1. The difference between arguments and parameters

# parametres are the variables that are defined
# or used inside parentheses when we deffine a function 
# the variable name and lastname inside the parenthesis are parametres
def print_name(name, lastname):
    print(name, lastname)

# The values passed for the parametre while
# calling the function is argument, therefore 
# the str, "Harry", "Potter" are the arguments here
print_name("Harry", "Potter")

# 2. Positional and keyword arguments
# We can call arguments by their names to make it more clear what they represent
# We can rearrange arguments in a way that makes them most readable

# positional args 
# "Harry" and "Potter" will automatically being
# considered as name and lastname based on their location 
print_name("Harry", "Potter")

# keyword args
# The order is not important here
print_name(name="Harry", lastname="Potter")
print_name(lastname="Potter", name="Harry")

# But these won't work 
# i. positional argument after keyword argument
# ii. multiple values for same argument
print_name(lastname="Potter", "Harry") 
print_name("Harry", name="Potter") 


# 3. Default arguments
# must be in the end, without exception

def mult_3_num(x, y, z=8):
    print((x ** y) * z)

# 4. Variable-length arguments (*args and **kwargs)
# If you mark a parameter with one asterisk (*), you can pass any number of positional arguments to your function (Typically called *args)
# If you mark a parameter with two asterisks (**), you can pass any number of keyword arguments to this function (Typically called **kwargs).

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

# The 3, 4, 5 are combined into args
# six and seven are combined into kwargs
foo(1, 2, 3, 4, 5, six=6, seven=7)
foo(1, 2, three=3)


# 5. Forced keyword arguments
# Sometimes you want to have keyword-only arguments. You can enforce that with:

# i. If you write '*,' in your function parameter list, all parameters after that must be passed as keyword arguments.
# ii. Arguments after variable-length arguments must be keyword arguments.

def foo(a, b, *, c, d):
    print(a, b, c, d)

foo(1, 2, c=3, d=4)
# not allowed:
# foo(1, 2, 3, 4)

# arguments after variable-length arguments must be keyword arguments
def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)

foo(8, 9, 10, last=50)
# missing 1 required keyword-only argument: 'last'
# foo(8, 9, 10, 50)
