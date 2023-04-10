
class Animal:
    def walk(self):
        print("walking")

class Mammal:
    def eat(self):
        print("eating")

# Dog inherits Animal, python supports multiple inheritance
class Dog(Animal, Mammal):
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("woof")

tom = Dog("Tom", 3)

print(type(tom))
print(tom.name)
print(tom.age)

tom.bark()
tom.walk()
tom.eat()
