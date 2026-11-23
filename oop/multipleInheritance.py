# Multiple inheritance = inherit from more than one parent class
# C(A, B)

# Multi level inheritance = inherit from a parent which inherits from another parent
# C(B) < B(A) < A


# Multi level

class Animal: 
    def eat(self):
        print("This animal is eating")

class Prey(Animal): 
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

        
# Multiple inheritance
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# Rabbits can only flee from Predators
rabbit.flee()

# Fish can either flee or hunt.
fish.flee()
fish.hunt()

