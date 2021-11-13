"""Our goal is to move all of the discs from tower A to tower C given the following constraints:

1. Only one disc can be moved at a time.
2. The topmost disc of any tower is the only one available for moving. 
3. A wider disc can never be atop a narrower disc.

modeling the tower: using stack (LIFO)

methods for stack:

push
pop

The import of Generic from the typing module enables Stack to be generic over a particular type in type hints. 

The arbitrary type T is defined in T = TypeVar('T'). T can be any type

1 Move the upper n-1 discs from tower A to B (the temporary tower), using C as the in-between.
2 Move the single lowest disc from A to C.
3 Move the n-1 discs from tower B to C, using A as the in-between.
"""

from typing import TypeVar, Generic, List 

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    
    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        self._container.pop()
    
    #  __repr__() is what will be output when print() is applied to a Stack.
    def __repr__(self) -> str:
        return repr(self._container)

# create the tower
num_discs: int= 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(1, num_discs + 1):
    tower_a.push(i)

# Solving the Towers of Hanoi -> Recursive
# Base case: moving one disc
# recursive case: moving more than one disc


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1: 
        end.push(begin.pop())
    else:
        print(f"tower_a: {tower_a}")
        hanoi(begin, temp, end, n - 1) 
        hanoi(temp, end, begin, n - 1)

if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)