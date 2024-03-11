from dataclasses import dataclass
@dataclass(frozen=True)
class Employee:
    name : str
    position : str
employee1 = Employee('John','Manager')
print(employee1)

employee1.name  = 'Denial'
print(employee1)