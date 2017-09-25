class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

def print_dog(dog):
    print(dog.name + "'s", 'age is', dog.age, 
                           'and weight is', dog.weight)

codie = Dog('Codie', 12, 38)
jackson = Dog('Jackson', 9, 12)
print_dog(codie)
print_dog(jackson)
