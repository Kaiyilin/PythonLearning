""""
This technique shows how a nested for loop in some problems can be 
converted to a single for loop to reduce the time complexity.

# Good for finding sub-string, and find the max value of sub-list
"""

# Brute force, using nested for loops

# code

import sys

print("GFG")

# O(n * k) solution for finding

# maximum sum of a subarray of size k

INT_MIN = -sys.maxsize - 1

# Returns maximum sum in a

# subarray of size k.

def maxSum(arr, n, k):

    # Initialize result
    
    max_sum = INT_MIN
    
    # Consider all blocks
    
    # starting with i.
    
    for i in range(n - k + 1):
    
        current_sum = 0
        
        for j in range(k):
        
            current_sum = current_sum + arr[i + j]
            
            # Update result if required.
            
            max_sum = max(current_sum, max_sum)
        
    return max_sum

# Driver code

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]

k = 4

n = len(arr)

print(maxSum(arr, n, k))


# O(n) solution for finding

# maximum sum of a subarray of size k

def maxSum(arr, k):

    # length of the array

    n = len(arr)

    # n must be greater than k

    if n < k:
        print("Invalid")
        return -1

    # Compute sum of first window of size k
    
    window_sum = sum(arr[:k])
    
    # first sum available
    
    max_sum = window_sum
    
    # Compute the sums of remaining windows by
    
    # removing first element of previous
    
    # window and adding last element of
    
    # the current window.
    
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]      
        max_sum = max(window_sum, max_sum)
    
    return max_sum

# Driver code

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]

k = 4

print(maxSum(arr, k))