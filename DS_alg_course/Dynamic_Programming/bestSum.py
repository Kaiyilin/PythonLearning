"""bestSum(targetSum, numbers)

the function should return an array contain the shortest
combination of numbers that add up to exactly the targetSum

If there is a tie for the shortest combination, you may return any one of the shortest
"""
from typing import List


def bestSum(targetSum: int, nums: List[int]) -> List[int]:
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    shortest_combination = None

    # iterate all the choices
    for num in nums:
        remainder = targetSum - num
        result = bestSum(remainder, nums)

        if result != None:
            combination = [*result, num]
        
        if shortest_combination == None or len(combination) < len(shortest_combination):
            shortest_combination = combination
    
    return shortest_combination
print(bestSum(7, [5, 3, 4, 7]))    
print(bestSum(8, [2, 5, 3]))    