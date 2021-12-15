from typing import Dict


def gridTraveler(row: int, column: int):

    # base case 
    if row == 0 or column == 0:
        return 0
    if row == 1 and column == 1:
        return 1
    
    return gridTraveler(row=row-1, column=column) + gridTraveler(row=row, column=column-1)


print(gridTraveler(2, 3)) # 3
# print(gridTraveler(18, 18)) # 2333606220, took too long 

# it will go to negative val
def gridTraveler_withMem0(row: int, column: int, memo={}):
    key = (row, column)
    # base case 
    if key in memo:
        return memo[key]

    if row == 0 or column == 0:
        return 0
    if row == 1 and column == 1:
        return 1
    
    memo[key] = gridTraveler_withMem0(row=row-1, column=column) + gridTraveler_withMem0(row=row, column=column-1)

    return memo[key]

print(gridTraveler_withMem0(18, 18))
