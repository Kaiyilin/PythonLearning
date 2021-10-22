import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# only shuffle the first axis
np.random.shuffle(arr)

# the numpy uses different seed method from python module, 
# so if you'd like to shuffle numpy module, make sure 
# uses random class of numpy

np.random.seed(1)
print(np.random.randint((5, 5)))
np.random.seed(2)
print(np.random.randint((5, 5)))