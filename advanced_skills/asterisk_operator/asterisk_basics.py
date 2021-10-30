"""The asterisk sign (*) can be used for different cases in Python:

Multiplication and power operations
Creation of list, tuple, or string with repeated elements
*args , **kwargs , and keyword-only parameters
Unpacking lists/tuples/dictionaries for function arguments
Unpacking containers
Merging containers into list / Merge dictionaries
"""

# 1. Multiplication and power operations

result = 7 * 5
power_result = 7 ** 5 

# 2. Creation of list, tuple, or string with repeated elements
# Take list for e.g. same rules are followed in tuple and string
rep_0 = [0] * 10
rep_none = [None] * 10
rep_twonums = [0, 1] * 5

# 3. *args , **kwargs , and keyword-only parameters
# see function_args folder

# 4. Unpacking lists/tuples/dictionaries for function arguments
def foo(a, b, c):
    print(a, b, c)

# length must match
my_list = [1, 2, 3]
foo(*my_list)

my_string = "ABC"
foo(*my_string)

# length and keys must match
my_dict = {'a': 4, 'b': 5, 'c': 6}
foo(**my_dict)


# 5. Unpacking containers
# Unpack the elements of a list, tuple, or set into single and multiple remaining elements.
# Note that multiple elements are combined in a list, 
# even if the unpacked container is a tuple or a set
numbers = (1, 2, 3, 4, 5, 6, 7, 8)

*beginning, last = numbers # The last element into one num, the rest to list
print(beginning)
print(last)

print()

first, *end = numbers # The first element into one num, the remain to list
print(first)
print(end)

print()
first, *middle, sec_last , last = numbers
print(first) # 1
print(middle) # [2, 3, 4, 5, 6]
print(last) # 8

# 6. Merging containers into list / Merge dictionaries

# dump iterables into a list and merge them
my_tuple = (1, 2, 3)
my_set = {4, 5, 6}
my_list = [*my_tuple, *my_set]
print(my_list)

# merge two dictionaries with dict unpacking
dict_a = {'one': 1, 'two': 2}
dict_b = {'three': 3, 'four': 4}
dict_c = {**dict_a, **dict_b}
print(dict_c)

# if the dictionaries have keys in common
# key-value in second dict will be the one after 
# merge with unpacking 
dict_a = {'one': 1, 'two': 2}
dict_b = {'two': 3, 'four': 4}
dict_c = {**dict_a, **dict_b}
print(dict_c)


# The above merging solution.
# It does not work if the dictionary has any non-string keys
dict_a = {'one': 1, 'two': 2}
dict_b = {3: 3, 'four': 4}
dict_c = dict(**dict_a, **dict_b)
print(dict_c)

# but it works fine in this.....
dict_a = {'one': 1, 'two': 2}
dict_b = {3: 3, 'four': 4}
dict_c = {**dict_a, **dict_b}
print(dict_c)