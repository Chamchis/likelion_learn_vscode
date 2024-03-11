import random

print(random.random())

print(random.randint(1, 100))

items = ['apple', 'banana', 'cherry', 'melon']

print(random.choice(items))

print(random.sample(items, 2))

print([random.choice(items) for i in range(10)])

print(items)
random.shuffle(items)
print(items)

print(random.seed(123))
print(random.random())