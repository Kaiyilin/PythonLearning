"""Outline
• The difference between arguments and parameters
• Positional and keyword arguments
• Default arguments
• Variable-length arguments (*args and **kwargs)
• Container unpacking into function arguments
• Local vs. global arguments
• Parameter passing (by value or by reference?)
"""

# 8. Parameter passing (by value or by reference?)

# Python uses a mechanism, which is known as "Call-by-Object" or "Call-by-Object-Reference. The following rules must be considered:
# for detail, check GeeksforGeeks https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/

# The parameter passed in is actually a reference to an object (but the reference is passed by value)
# Difference between mutable and immutable data types

# This means that:

# Mutable objects (e.g. lists,dict) can be changed within a method.
#   • But if you rebind the reference in the method, the outer reference will still point at the original object.
# Immutable objects (e.g. int, string) cannot be changed within a method.
#   • But immutable object CONTAINED WITHIN a mutable object can be re-assigned within a method.


# immutable obj --> no change 
def shift(x):
    x += 5 #x is immutable and a new variable must be created

var = 10
print('var before shift():', var)
shift(var)
print('var after shift():', var)

# mutable ogj --> change
# mutable objects -> change
def foo(a_list):
    a_list.append(4)
    
my_list = [1, 2, 3]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)


# immutable objects within a mutable object -> change
def shift_list(x: list) -> list:
    x[0] += 5
    x[1] = "string"
my_list = [5, 4, 3]
print('var before shift_list():', my_list)
shift_list(my_list)
print('var after shift_list():', my_list)


# Rebind a mutable reference -> no change
# Be careful with += and = operations for mutable types. 
# The first operation has an effect on the passed argument while the latter has not
def foo(a_list):
    a_list = [50, 60, 70] # a_list is now a new local variable within the function, it won't chang unless you return
    a_list.append(50)
    
my_list = [1, 2, 3]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)

# another example with rebinding references:
def foo(a_list):
    a_list += [4, 5] # this chanches the outer variable
    
def bar(a_list):
    a_list = a_list + [4, 5] # this rebinds the reference to a new local variable

my_list = [1, 2, 3]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)

my_list = [1, 2, 3]
print('my_list before bar():', my_list)
bar(my_list)
print('my_list after bar():', my_list)