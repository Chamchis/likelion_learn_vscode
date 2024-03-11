class Box:
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
    def __lt__(self.other):
        return self.width*self.height
box1 = Box(3,5)
box2 = Box(2,6)

print(box1 > box2)
