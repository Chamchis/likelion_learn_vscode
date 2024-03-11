# super
class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print('나는 {} 입니다.'.format(self.name))

person = Person('일론 머스크')
person.introduce()

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    def introduce(self):
        super().introduce()
        print(f'내 학번은 {self.student_id}번 입니다.')


student = Student('희성',1)
student.introduce()