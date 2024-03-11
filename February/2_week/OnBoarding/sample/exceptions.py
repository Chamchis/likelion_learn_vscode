# 예외(Exceptions)

# a = 10
# b = 0
# a / b 

fruits = ['apple', 'banana', 'strawberry']
try:
    fruits_1 = fruits[3]
except:
    print('인덱스를 참조할 수 없습니다. ')
else:
    print(fruits_1)
finally:
    print('수행 완료')

print(fruits)