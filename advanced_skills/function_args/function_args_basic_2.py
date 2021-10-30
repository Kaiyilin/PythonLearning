"""Outline
• The difference between arguments and parameters
• Positional and keyword arguments
• Default arguments
• Variable-length arguments (*args and **kwargs)
• Container unpacking into function arguments
• Local vs. global arguments
• Parameter passing (by value or by reference?)
"""

# 6. Container unpacking into function arguments

def print_name(name, last_name, middle_name):
    print("I am", name, middle_name,last_name)

# len of the container must meet the num of parametres in the func
# it worlks on tuple as well 
name = ["Tom", "Riddle", "Voldemort"]

print_name(*name)

# use dict, the key must match the name of parametres
name_dict = {
    "name" : "Tome", 
    "last_name" : "Riddle",
    "middle_name" : "noNose"
}
print_name(**name_dict)

# 7. Local vs. global arguments
# Global variables can be accessed within a function body, but to modify them,
# we first must state global var_name in order to change the global variable.

def foo1():
    x = number # global variable can only be accessed here
    print('number in function:', x)

number = 0
foo1()

# modifying the global variable
def foo2():
    global number # global variable can now be accessed and modified
    number = 3

print('number before foo2(): ', number)
foo2() # modifies the global variable
print('number after foo2(): ', number)

#  If we do not write global var_name and asign a new value to a variable
#  with the same name as the global variable,
#  this will create a local variable within the function. The global variable remains unchanged.
def foo3():
    number = 3 # this is a local variable
print('number before foo3(): ', number)
foo3() # does not modify the global variable
print('number after foo3(): ', number)

# 8. Parameter passing (by value or by reference?)
