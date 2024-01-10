from enum import Enum, unique, auto
from typing import Any

@unique
class Vendors(Enum):
    AWS  = auto()
    AZURE = auto()
    GCP = auto()

class Person():
    def __init__(self, fName, lName, age) -> None:
        self.fName = fName
        self.lName = lName
        self.age = age
    
    def __str__(self) -> str:
        '''return string for the object'''
        return self.fName + ' ' + self.lName + ' ' + self.age

def runProgram():
    print('advanced classes:')
    roy = Person('roy', 'bro', '30')
    print(roy)
