"""Our maze will be a two-dimensional grid of Cells. 
A Cell is an enum with str values 

" " : empty space 
"X" : blocked space.

Note:

conventionally, a private function (cannot be used outside the class starts with _)
"""

from enum import Enum
from typing import (
    List, 
    NamedTuple,
    Callable,
    Optional,
    Generic, 
    TypeVar
)
import random
from math import sqrt
from generic_srch import dfs, bfs, node_to_path, astar, Node

# In CS, an enumerated type is a dtype consisting of a set of named values called elements, 
# members, enumeral, or enumerators of the type. An enumeration is used in any 
# programming language to define a constant set of values. 

class Cell(str, Enum):
    """ Cell is defined to represent 
    a constant set of values. 

    Conventionally, the constant often represent in UPPERCASE
    """
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    """ MazeLocation is a named tuple object
    The named tuple object assign meaning 
    to each position in a tuple 
    and allow for more readable, self-documenting code.

    Usage example:
    
    MazeLocation(0, 1)
    print(MazeLocation.row) -> 0
    print(MazeLocation.column) -> 1 

    """
    row: int
    column: int

class Maze:
    def __init__(self, 
                 rows: int=10, 
                 columns: int=10, 
                 sparsenss: float=0.2,
                 start: MazeLocation=MazeLocation(0,0),
                 goal: MazeLocation=MazeLocation(9,9)) -> None:
        """
        rows: int=10, 
        columns: int=10, 
        sparsenss: float=0.2,
        start: MazeLocation=MazeLocation(0,0),
        goal: MazeLocation=MazeLocation(9,9)
        """
        
        # initiate basic instance variables
        self._rows = rows
        self._columns = columns
        self._sparsness = sparsenss
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        # generate empty cells
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for row in range(rows)]
        self._radomly_fill(rows, columns, sparsenss)
        # fill the start and goal locations in 
        self._grid[start.row][start.column] = Cell.START 
        self._grid[goal.row][goal.column] = Cell.GOAL
    
    def _radomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED
    
    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n" 
        return output

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal
    
    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        """checks above, below, to the right, 
        and to the left of a MazeLocation in a Maze 
        to see if it can find empty spaces that can be gone to from that location.
        """
        locations: List[MazeLocation] = []
        # check the right
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        # check the left    
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        # check the above    
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        # check the below
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))
        return locations

    def mark(self, path: List[MazeLocation]): 
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        for maze_location in path: 
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

if __name__ == "__main__":
    # Test DFS
    m: Maze = Maze()
    print(m)
    solution1: Optional[Node[MazeLocation]] = dfs(m.start, m.goal_test, m.successors)

    if solution1 is None:
        print("No solution found using depth-first search!") 
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        m.mark(path1)
        print(m)
        m.clear(path1)
    
    solution2: Optional[Node[MazeLocation]] = bfs(m.start, m.goal_test, m.successors)
    if solution2 is None:
        print("No solution found using breadth-first search!") 
    else:
        path2: List[MazeLocation] = node_to_path(solution2)
        m.mark(path2)
        print(m)
        m.clear(path2)
