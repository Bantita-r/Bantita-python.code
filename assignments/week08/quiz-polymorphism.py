"""
Demonstrate polymorphism by creating:

    A base class Animal with method move()
    Three derived classes: Fish, Bird, Dog with different implementations of move()
        fish swims, bird flies, dog runs
    A function that takes any animal and calls its move() method
"""
class Animal:
   def move(self):
       raise NotImplementedError("Subclass must implement abstract method")

class Fish(Animal):
   def move(self):
       return "The fish swims in the water."

class Bird(Animal):
   def move(self):
       return "The bird flies in the sky."

class Dog(Animal):
   def move(self):
       return "The dog runs on the ground."

def animal_move(animal: Animal):
   print(animal.move())
