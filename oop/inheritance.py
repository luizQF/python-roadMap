# Allows a class to inherit attributes and methods from another class 
# Helps with code reusability and extensibility
# class Child(parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_aline = True

    def eat(self):
        print(f"{self.name} is eating")

# The dog is inheriting all attributes and methods from Animal.
class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog1 = Dog("Frenzy")

cat1 = Cat("Lazy")

print(dog1.name)
dog1.eat()