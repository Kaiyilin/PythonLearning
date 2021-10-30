"""Use Leibniz formula

pi = 4/1 - 4/3 + 4/5 - 4/7 +4/9 - 4/11...

in computer you can write as 

(1 * (4 / 1)) + ((-1) * (4 / 3)) + (1 * (4 / 5)) 

one const (operation) chages periodically
denominator + 2 every single operation 

On most platforms, Python floats are 64-bit floating-point numbers (or double in C).

example of how rote conversion between formula and programmatic code 
can be both simple and effective in modeling or simulating an interesting concept.

but keep in mind that it is not necessarily the most efficient solution.
"""

# can be implemented with more efficient or compact code.
def cal_pi(num_repeated):
    numerator : float = 4.0
    denominator: float = 1.0
    operation: float = 1.0 
    pi_num: float = 0.0
    for _ in range(num_repeated):
        pi_num += operation * (numerator / denominator)
        operation *= (-1.0)
        denominator += 2.0
    return pi_num

if __name__ == "__main__":
    print(cal_pi(50))