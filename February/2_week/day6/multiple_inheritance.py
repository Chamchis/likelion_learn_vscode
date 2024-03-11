# 다중상속
class Base1:
    def __init__(self):
        print('Base1의 __init__ 실행')
        super().__init__()
class Base2:
    def __init__(self):
        print('Base2의 __init__ 실행')
        super().__init__()
class Child(Base1,Base2):
    def __init__(self):
        print('Child의 __init__ 실행')
        super().__init__()

child = Child()