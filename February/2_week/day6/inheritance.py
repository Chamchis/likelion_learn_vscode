# 상속

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        # print('{}의 울음소리를 냅니다.'.format(self.name))
        raise NotImplementedError('아직 구현이 안되었어요')

class Dog(Animal):
    def speak(self):
        print('바우바우!')

class Cat(Animal):
    def speak(self):
        print('냥냥!')
    def playing(self):
        print('재미있게 놉니다')

dog = Dog('dog')
cat = Cat('cat')

dog.speak()
cat.speak()
cat.playing()