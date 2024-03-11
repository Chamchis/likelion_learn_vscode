from collections import deque
d = deque(['task1','task2','task3'])
d.append('task4')
print(d)
print(d.pop())
print(d)
a = ['task1','task2','task3']
print(a)
print(a.append('task4'))
print(a)
print(a.pop(0))
print(a)
d = deque([i for i in range(10000)])
for i in range(1000):
    d.pop()

