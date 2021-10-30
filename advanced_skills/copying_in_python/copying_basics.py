"""Shallow vs deep copying¶

In Python, assignment statements (obj_b = obj_a) do not create real copies. 
It only creates a new variable with the same reference. VVV Remember this

So when you want to make actual copies of mutable objects (lists, dicts) and want to modify the copy without affecting the original, you have to be careful.
For 'real' copies we can use the copy module. 
However, for compound/nested objects (e.g. nested lists or dicts) and 
custom objects there is an important difference between shallow and deep copying:

shallow copies: Only one level deep. It creates a new collection object and populates it with references to the nested objects. 
This means modyfing a nested object in the copy deeper than one level affects the original.

deep copies: A full independent clone. 
It creates a new collection object and then recursively populates it with copies of the nested objects found in the original.
"""
import copy

# deal with immutable type, the copy will change to 6 
# without affect the origin
origin = 5
cpy = origin
print(id(cpy) == id(origin)) # True, point to same ref
cpy = 6 
print(id(cpy) == id(origin)) # False, point to dif ref

# careful when you deal with mutable type, like list, set, dict
# this will affect the original that's bcuz python did not make a real copy
origin = [5, 4, 3, 2, 1]
cpy = origin
print("before modification:", "\n", origin, "\n", cpy)
cpy[0] = 6 
print("after modification:", "\n", origin, "\n", cpy) 

# for a real copy, you can use copy module
# - shallow copy: one level deep, inly ref of nested child objects
# - deep copy: full independent copy

# shallow copy
origin = [5, 4, 3, 2, 1]
cpy = origin.copy() # or copy.copy(original)
print("before modification:", "\n", origin, "\n", cpy)
cpy[0] = 6 
print("after modification:", "\n", origin, "\n", cpy) 

# what if we have a list inside a list??
# the origin still affected by the modification! 
origin = [[5, 4, 3], [2, 1, 0]]
cpy = origin.copy() # or copy.copy(original)
print("before modification:", "\n", origin, "\n", cpy)
cpy[0][0] = 6 
print("after modification:", "\n", origin, "\n", cpy) 

# deep copy helps you solve that problem
origin = [[5, 4, 3], [2, 1, 0]]
cpy = copy.deepcopy(origin) # or copy.copy(original)
print("before modification:", "\n", origin, "\n", cpy)
cpy[0][0] = 6 
print("after modification:", "\n", origin, "\n", cpy) 
