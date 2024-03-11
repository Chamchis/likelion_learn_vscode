class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):

    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Max")
cat = Cat("Felix")

print(dog.speak())  # Max says Woof!
print(cat.speak())  # Felix says Meow!