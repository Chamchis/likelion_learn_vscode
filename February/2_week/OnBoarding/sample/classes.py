# # 클래스(Class) - 설계

# class Student:

#     def __init__(self, name, major):
#         self.name = name
#         self.major = major
#         self.is_graduated = False
#     def study(self):
#         print(f'{self.name} 학생은 공부 중입니다. ')

#     def edit_major(self, new_major):
#         student_1.major  = new_major
#         print(f'{student_1.major}로 전공이 변경되었습니다. ')

# # 인스턴스 - 실체화된 화물
        
# student_1 = Student('김준호', '컴퓨터과학과')

# # student_1.major = '기계공학과'
# student_1.edit_major('전기공학과')


# print(student_1.major)

# # 상속(Inheritance)

# class ForeignStudent(Student):

#     def __init__(self, name, major, country):
#         super().__init__(name, major)
#         self.country = country

#     # 오버라이딩
#     def study(self):
#         print(f'{self.name} is studying now. ')

# foreign_stud_1 = ForeignStudent('이주노', '프랑스어학과', 'United Kingdom')
# # print(foreign_stud_1.name)
# # print(foreign_stud_1.major)
# # print(foreign_stud_1.country)
# # print(foreign_stud_1.is_graduated)
# foreign_stud_1.study()