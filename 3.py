# The @property decorator in Python allows you to define a method as a property, enabling you to use it like an attribute. 
# This provides a way to define getter, setter, and deleter methods for class attributes,
# giving you control over how an attribute is accessed or modified without changing how it’s used.

# Basic Use of @property
# The @property decorator is typically used to define a getter method, making an internal method behave like a regular attribute.
# Example:
class Circle:
    def __init__(self, radius):
        self._radius = radius  # The underscore signifies that it's intended to be "private"
    
    @property
    def radius(self):
        """Getter for the radius property"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter for the radius property"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        """Computed property for the area"""
        return 3.1416 * (self._radius ** 2)

# Usage
c = Circle(5)
print(c.radius)  # Calls the getter: Output -> 5
print(c.area)    # Calls the computed property: Output -> 78.53999999999999

c.radius = 10    # Calls the setter
print(c.area)    # Output -> 314.16

# c.radius = -1   # Raises ValueError
# Key Concepts:
# Getter (@property): When you use @property, it allows you to access a method like an attribute.

# In the example above, radius is accessed as c.radius without needing to call c.radius().
# Setter (@radius.setter): Defines the method to set the value of the property. You use the same name as the property decorated with @property, but with .setter.

# In the example, setting c.radius = 10 triggers the setter method.
# Deleter (@radius.deleter): If you want to delete a property, you can use the @propertyname.deleter decorator.

# @radius.deleter
# def radius(self):
#     del self._radius
# Advantages of Using @property
# Encapsulation: Properties allow you to control access to instance attributes while keeping the interface clean.
# Computed Attributes: You can create attributes that are computed on the fly (e.g., area in the above example).
# Backward Compatibility: If you initially used a public attribute and later want to add validation or logic, you can convert it to a property without breaking existing code.
# Example with a Deleter:

class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value
    
    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

# Usage
p = Person("Alice")
print(p.name)  # Output -> Alice
p.name = "Bob"
print(p.name)  # Output -> Bob
del p.name     # Calls the deleter, Output -> Deleting name...
# When to Use @property:
# When you need to add logic when getting or setting an attribute (e.g., validation).
# When you want an attribute that computes its value dynamically based on other attributes.