from typing import List


# brute force 
def canSum(targetSum: int, nums: List[int]) -> bool:
    
    if targetSum == 0:
        return True
    
    # MAKE SURE YOU CAN HANDLE THE NEGATIVE ISSUE
    if targetSum < 0:
        return False
    
    for num in nums:
        remainder = targetSum - num

        # if you get ine way, you succeed it
        if canSum(remainder, nums) == True:
            return True
    
    # if you srch out all the possibilities, and never get true
    # return false 
    return False


print(canSum(7, [2, 3])) # True
#print(canSum(300, [7, 14])) # false, lacks of efficiency

# add memorisation
def canSum(targetSum: int, nums: List[int], memo={}) -> bool:
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return True
    
    # MAKE SURE YOU CAN HANDLE THE NEGATIVE ISSUE
    if targetSum < 0:
        return False
    
    for num in nums:
        remainder = targetSum - num

        # if you get ine way, you succeed it
        if canSum(remainder, nums) == True:
            memo[targetSum] = True
            return True
    
    # if you srch out all the possibilities, and never get true
    # return false 
    memo[targetSum] = False
    return False


print(canSum(7, [2, 3])) # True
print(canSum(300, [7, 14])) # false, lacks of efficiency
