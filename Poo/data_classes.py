from dataclasses import dataclass
from typing import ClassVar

@dataclass
class User:
    
    first_name: str 
    last_name: str
    count_user: ClassVar[int]
    major: bool 
    age: int
    
    def __post_init__(self):
        self.full_name = f"{self.first_name}  {self.last_name}"
        

    
    
jeff = User("Jeef", "Karmaka", True, 6)
print(jeff.__dict__)
print(jeff)
print(jeff.full_name)
