from typing import List


def howSum(targetNum: int, nums: List[int]) -> List[List[int]]:
    """given a targetSum, and an array nums
    return possible combinations if element in nums can add up as targetNum
    else return None
    """
    # base cases
    if targetNum == 0:
        return []
    
    if targetNum < 0:
        return None
    
    for num in nums:
        remainder = targetNum - num
        remainder_result = howSum(remainder, nums) # find whether remainder in the nums or not

        if remainder_result != None:
            result = [*remainder_result, num]
            return result
    
    return None

print(howSum(8, [2, 3, 4, 7]))

def howSum(targetNum: int, nums: List[int], memo={}) -> List[List[int]]:
    """given a targetSum, and an array nums
    return possible combinations if element in nums can add up as targetNum
    else return None
    """
    if targetNum in memo:
        return memo[targetNum]
    # base cases
    if targetNum == 0:
        return []
    
    if targetNum < 0:
        return None
    
    for num in nums:
        remainder = targetNum - num
        remainder_result = howSum(remainder, nums) # find whether remainder in the nums or not

        if remainder_result != None:
            memo[targetNum] = [*remainder_result, num]
            return memo[targetNum]
    
    memo[targetNum] = None
    return None

memo = {}
#print(howSum(8, [2, 3, 4, 7], memo=memo))
#print(howSum(300, [7, 14], memo=memo))
print(howSum(300, [2, 14], memo=memo))