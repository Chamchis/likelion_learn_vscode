# class ClassStatic:
#     @staticmethod
#     def check():
#         print('hello')

# ClassStatic.check()

class initNeed:
    number = 0
    def __init__(self):
        number_instance = 10
    @classmethod
    def get(cls):
        return cls.number
    def cls_number_val(self,val):
        initNeed.number = val

a = initNeed()
b = initNeed()

b.cls_number_val(999)
print(a.number)
print(b.number)