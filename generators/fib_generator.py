def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib_30 = fib(30)
for i in fib_30:
    print(i)