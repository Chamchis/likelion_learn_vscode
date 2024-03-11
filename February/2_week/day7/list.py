# 가변 타일 필드 사용때 이렇게 하면 됩니다.
from dataclasses import dataclass, field
@dataclass
class StudentCourses:
    name : str
    courses : list = field(default_factory=list)

student10 = StudentCourses('Daniel')
student10.courses.append('Math')
student10.courses.append('Physics')
print(student10)