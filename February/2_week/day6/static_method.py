# Static Method
# class Math:
#     def add(self,x,y):
#         return x + y
# math = Math()
# print(math.add(3,5))

class Math:
    @staticmethod
    def multiple(x,y):
        return x * y
math = Math()
print(math.multiple(3,8))