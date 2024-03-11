class Student:
    def __init__(self,name,age,major) -> None:
        self.name = name
        self.age = age
        self.major = major
student_original = Student('이름',17,'전공')

print(student_original.name)
        
from dataclasses import dataclass
@dataclass
class Student_dc:
    name : str
    age : int
    major : str

student1 = Student_dc('멋사',30,'IT')
print(student1)
