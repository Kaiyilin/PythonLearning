"""
Lambda is used when you only want to use certain function once

You can simply create that function in one line of code instead of a 2-4 lines function
"""

# Example Suggest you want add 10
add_10 = lambda x: x+10
print(add_10(x = 10))

mul = lambda x, y: x*y
print(mul(5,6))

# sort array based on second element
arrays = [(1,2),(55,8),(33,68), (5,43), (9,12)]
# Based on first element
print(sorted(arrays))
# Based on second element
print(sorted(arrays, key= lambda x: x[1]))
# Based on the sum 
print(sorted(arrays, key= lambda x: x[0] + x[1]))

# map func
another_array = [i for i in range(60)]
another_array_mul2 = map(lambda x: x*2, another_array)
print(another_array, "\n", list(another_array_mul2)) # convert to list for display

# Another way is 
another_array_mul2_v2 = [x*2 for x in another_array]
print(another_array_mul2_v2)

# filter func, again you can achieve this with list comprehension
fil_array = filter(lambda x: x <5, another_array)
fil_array_2 = filter(lambda x: x//5 == 1, another_array) # [x for x in another_array if x//5 ==1]
print(list(fil_array))
print(list(fil_array_2))