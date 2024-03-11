class A:
    def __init__(self,name,courses = None) -> None:
        self.name = name
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

a = A('a')
print(a.courses)
b = A('b')
print(b.courses)

a.courses.append('Good')
print(a.courses)
print(b.courses)
