# CONFIDENCE INTERVALS

import numpy as np
from dataclasses import dataclass
from enum import Enum, auto

# _________________m&m's Sample Data_________________
# Variables   : Color(Categorical) 
# Sample      : Red, Blue, blue, Red, Red, Yellow, Blue, Red, Blue, Gree, Brown, Yellow, Red, Brown, Blue, Green
# Observations: 35
# ___________________________________________________

class Colors(Enum):
    RED    = auto()
    BLUE   = auto()
    GREEN  = auto()
    YELLOW = auto()
    BROWN  = auto()
    

@dataclass
class Variable:
    name:    str
    outcome: int

@dataclass
class Observation:
    id: int
    var_data: list[Variable]

class Sample:
    def __init__(self):
        self.data:  Map[Observation] = {} # Sameple is a set of Observations
        self.n: int = 0 # Sample Size

    def add_data(self, var_data: list[Variable]):
        data_point = Observation(self.n, var_data)
        self.data[self.n] = data_point
        self.n+=1

def main():
    print("I may not be confident, but I can still compute confidence intervals! x3")

    color_blue = Variable("Color", Colors.BLUE.value)
    
    mnm_sample = Sample()
   
    for _ in range(50):
            variables = [color_blue]
            mnm_sample.add_data(variables)


if __name__ == "__main__":
    main()
