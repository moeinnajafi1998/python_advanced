# In Python, multiple inheritance refers to a feature where a class can inherit from more than one base class. 
# This means a subclass can have multiple parent classes and inherit attributes and methods from all of them.
# Syntax
class Parent1:
    def method_1(self):
        print("Method 1 from Parent1")

class Parent2:
    def method_2(self):
        print("Method 2 from Parent2")

class Child(Parent1, Parent2):
    def method_3(self):
        print("Method 3 from Child")
# Creating an instance of Child class
child_instance = Child()
child_instance.method_1()  # From Parent1
child_instance.method_2()  # From Parent2
child_instance.method_3()  # From Child

# In the example above, the Child class inherits from both Parent1 and Parent2. Thus, it can access methods from both parents.

# Method Resolution Order (MRO)
# When a class inherits from multiple classes, Python follows a specific order in which it looks for methods and attributes, called the Method Resolution Order (MRO). 
# This order can be viewed using the mro() method or the __mro__ attribute:
print(Child.mro())
# Output: [<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>]
# The MRO helps resolve any conflicts that may arise if multiple parent classes have methods with the same name.
# Diamond Problem
# The diamond problem occurs when a class inherits from two classes that both inherit from a common base class, leading to potential ambiguity. 
# Python handles this with MRO, ensuring that a method from the most specific class is called.
class A:
    def method(self):
        print("Method from A")

class B(A):
    def method(self):
        print("Method from B")

class C(A):
    def method(self):
        print("Method from C")

class D(B, C):
    pass

d = D()
d.method()  # Output: "Method from B" (MRO: D -> B -> C -> A)
# In this case, Python uses the C3 linearization algorithm to resolve the MRO and call the method in B first.

# Advantages
# Code reuse: You can combine functionality from multiple parent classes.
# Flexibility: Allows a class to model complex behaviors by inheriting from several base classes.
# Disadvantages
# Complexity: It can make code harder to understand due to potential ambiguities or conflicts.
# Conflicting method names: If multiple parent classes define the same method, it could lead to unexpected behavior.