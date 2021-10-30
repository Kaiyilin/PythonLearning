import random

# obtain a random num 
a = random.random()

# obtain a random int num in range [a, b) or [a, b]
# return float
a = random.uniform(a=0, b=10)

# obtain a random num of normal distribution
a = random.normalvariate(mu=0, sigma=1)

# obtain a random int num in range [a, b]
# which includes both endpoints
a = random.randint(a=0, b=10)

# obtain a random num from range 
# which not includes the endpoints
a = random.randrange(start=0, stop=10)

# obtain a random pick an unique in the given sequence data structure (list, tuple)
sample_list = [1, 2, 3, 4 , 5 , 65, 8, 77, 10]
a = random.choice(sample_list)

# obtain a random pick a k-sized list in the 
# given sequence data structure (list, tuple) with replacement
# the elements can be picked multiple times
a = random.choices(sample_list, k=3)
a = random.choices(sample_list, k=100) # still work

# sampling the given sequetial ds, 
# to a k-size unique elements will never pick same element twice
a = random.sample(sample_list, k=100) # > len(sample_list), error
a = random.sample(sample_list, k=5)

# random shuffling the given ds in place, without retuning anything
random.shuffle(sample_list)

# The random in computer is actually pseudo-random 
# you can use seed method to reproduce the result
# a is a int
random.seed(a=1)
print(random.random())
print(random.randint(1, 50))

# re-seed to obtain same result
random.seed(a=1)
print(random.random())
print(random.randint(1, 50))

# different result if you put seed differently
random.seed(a=2)
print(random.random())
print(random.randint(1, 50))

# for pwd, you don't want it to be seedable (hashable) 
# in this case, you can use secrets module for 
# cryptographically strong pseudo-random numbers suitable for 
# managing secrets such as account authentication, tokens, and similar.