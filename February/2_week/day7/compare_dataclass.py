from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int

point1 = Point(5, 10)
point2 = Point(5, 10)
point3 = Point(3, 4)

print(point1 == point2)  # True
print(point1 == point3)  # False