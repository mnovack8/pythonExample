class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):

    def __init__self(self):
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


dog = Mammal()
print(dog.age)
print(dog.weight)
dog.eat()
dog.walk()
