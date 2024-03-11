from dataclasses import dataclass

# @dataclass

# class Student:
#     name : str
#     age : int
#     major : str
# student1 = Student('Saint',22,'OpenAi')
# print(student1)

# class Student_1:
#   def __repr__(self):
#     return "데이터클래스의 차이를 볼까요?"

# st = Student_1()
# print(st)


@dataclass

class Student:
    name : str
    age : int
    major : str

    def __post_init__(self):
        if not isinstance(self.age,int):
            raise TypeError('연령은 정수로 입력되어야 합니다.')
student1 = Student('Saint',33,'OpenAi')
student2 = Student('James',24,'kakao')
student3 = Student('Denial',27,'pyonkiti')
print(student1)
print(student2 == student3)

class Student_1:
  def __init__(self, name, age, major):
    self.name = name
    self.age = age
    self.major = major
student3_1 = Student_1("태연", 25, "카카오")
student4_1 = Student_1("태연", 25, "카카오")
print(student3_1 == student4_1)

student5_1 = Student("태연", 25, "카카오")
student6_1 = Student("태연", 25, "카카오")
print(student5_1 == student6_1)
student6_1.major = ('Google')
print(student6_1)
