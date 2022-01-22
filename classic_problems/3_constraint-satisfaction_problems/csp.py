from typing import (
    Generic,
    TypeVar,
    Dict,
    List,
    Optional
    )
from abc import (
    ABC,
    abstractclassmethod
)

V = TypeVar("V") # variable type
D = TypeVar("D") # domain type

# Base class for all constraints

class Constraint(Generic[V, D], ABC):
    # The variables that the constraint is between

    def __init__(self, variables: List[V]) -> None:
        self.variables = variables
    
    # Must be overridden by subclasses
    # Abstract base classes serve as templates for a class hierarchy.
    @abstractclassmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...

class CSP(Generic[V, D]):
    def __init__(self, varaibles: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = varaibles # variables to be constrained
        self.domains: Dict[V, List[D]] = domains # domains of each variables
        self.constraints = {}

        for variable in self.varaibles:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigment")