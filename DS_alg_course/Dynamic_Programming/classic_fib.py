
def fib(n):
    table = {
        0 : 0,
        1 : 1,
        2 : 1
    }

    for i in range(3, n + 1):
        table[i] = table[i-2] + table[i-1]

    return table[n] 