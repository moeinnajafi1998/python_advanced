# In Python, abstract classes and interfaces are not explicitly distinct as in some other languages (e.g., Java). 
# However, Python provides the concept of abstract classes via the abc (Abstract Base Classes) module, which can be used to simulate interface-like behavior. 
# Here's a breakdown of how abstract classes and interfaces compare in Python:

# 1. Abstract Classes
# Purpose: An abstract class is a class that cannot be instantiated and is meant to be subclassed. It defines a common interface for a group of subclasses.
# Use case: When you want to share common behavior and also define some methods that must be implemented by the subclasses.
# Implementation: Use the abc.ABC class and the @abstractmethod decorator to define abstract methods. These must be implemented in any non-abstract subclass.
# Example:
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# dog = Animal()  # This would raise an error
dog = Dog()  # Valid
dog.sound()  # Output: Bark
dog.eat()    # Output: This animal is eating

# Partial implementation: Abstract classes can have both fully implemented methods (like eat() in the example above) and abstract methods.
# Instantiation: You cannot instantiate an abstract class directly.
# 2. Interfaces (Simulated using Abstract Classes)
# Purpose: Python does not have an explicit interface construct, but abstract classes can simulate interfaces. In an interface, 
# all methods are abstract (i.e., no concrete methods), and it defines a strict contract for subclasses.
# Use case: Use when you only want to define method signatures without any implementation, and the implementation must be provided by the subclass.
# Example:

from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird(Movable, Flyable):
    def move(self):
        print("Bird is moving")

    def fly(self):
        print("Bird is flying")

bird = Bird()
bird.move()  # Output: Bird is moving
bird.fly()   # Output: Bird is flying
# All methods abstract: In an interface-like class, every method is an abstract method.
# No instantiation: Like abstract classes, these "interface" classes cannot be instantiated directly.
# Key Differences:
# Abstract classes can have both abstract and concrete methods, whereas interfaces (if simulated) would only define abstract methods.
# Abstract classes can be used to provide default behavior, while interfaces are more about enforcing a contract with no predefined behavior.
# Similarities:
# Both abstract classes and interfaces (simulated) define a structure for subclasses to follow.
# Both can use multiple inheritance in Python.
# In short, in Python, interfaces can be emulated using abstract classes by ensuring that all methods are abstract, 
# while abstract classes can also provide some default implementations.