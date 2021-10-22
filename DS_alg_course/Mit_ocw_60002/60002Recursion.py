"""
PseudoCode
function recursive(input):
    if input <= 0:
        return input 
    else:
        output = recursive(input -1)
        return output
"""

def get_fib(position):
    fib = {}
    if position == 0 or position == 1:
        return 1
    try: 
        return fib[position]
    except KeyError:
        result = get_fib(position - 1) + get_fib(position - 2) 
        fib[position] = result
        return result

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
