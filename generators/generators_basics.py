import sys
"""function that return an obj that can be iterated over
they generate the items inside the obj lazily
i.e. they generate the items only one at a time and only when you ask for it.
memory efficient

like normal function, use yield statement instead of return statement
"""

def mygenerator():
    yield 1
    yield 2 
    yield 3

g = mygenerator()

for i in g:
    print(i)

g = mygenerator()

# Will stop iteration if it does not reach another yield statement
# in this case, stop iteration in 4th times 
val = next(g)
print(val)

# sum up the value of generator
sum(g)

# created a sorted list of our generator
sorted(g)

def countdown(num):
    print("Starting")
    while num > 0:
        yield num 
        num -= 1

cd = countdown(5)
val = next(cd)
print(val)

"""The meaning of generator is it saves memory space!

The following 2 method works identical
suggest you'd like to get some indices from 1 to n

from sys module you can see that method 2 saves space
and the pros of method 2 is that you don't have to wait the whole loop 
to do the calculation 
"""
# method 1, create a list, 
# store each value then cal the list
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# method 2, use generator
# yield the number iteratively

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1 

# 200 bytes
print(sys.getsizeof(firstn(10))) 
# 1.49s
sum(firstn(10000000))  

# 128 bytes
print(sys.getsizeof(firstn_generator(10)))
# 859 ms
sum(firstn_generator(10000000))

"""Last example, you can use generator to create a list
using generator saves memory space, you can converted the 
gen to list when you need it in list  
"""
my_gen = (i for i in range(10000000) if i % 2 == 0)
print(sys.getsizeof(my_gen)) # 128 bytes

the_list = list(my_gen)
print(sys.getsizeof(the_list)) # 42915456 bytes

my_list = [i for i in range(10000000) if i % 2 == 0]
print(sys.getsizeof(my_list)) # 40215176 bytes

print(the_list == my_list) # True