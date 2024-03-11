class Person:
    population = 0

    def __init__(self,name):
        self.name = name
        Person.population +=1
    @classmethod
    def get_population(cls):
        return cls.population
    @classmethod
    def create_anonymous(cls):
        return cls('Anonymous')

John = Person('John')
print(John.get_population())
Jane = Person('John')
print(Jane.get_population())

anonymous = Person.create_anonymous()
print(anonymous)

