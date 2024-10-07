# Let's dive into Decorators and Context Managers in Python.
# 1. Function Decorators
# A decorator in Python is a function that modifies the behavior of another function. 
# It's typically used for code reuse, logging, access control, memoization, and more. Decorators are often implemented as higher-order functions.
# Example:
def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print(f"Wrapper executed before {original_func.__name__}")
        result = original_func(*args, **kwargs)
        print(f"Wrapper executed after {original_func.__name__}")
        return result
    return wrapper_func

@decorator_func
def display():
    print("Display function ran")
display()

# In this example, decorator_func wraps around display(). The @decorator_func syntax is equivalent to display = decorator_func(display).

# Common Use Cases:
# Timing: Measuring how long a function takes to execute.
# Logging: Automatically logging when a function is called.
# Access Control: Checking if a user has permissions before running certain code.
# 2. Class Decorators
# Class decorators are similar to function decorators but they operate on classes instead of functions. They can be used to modify class definitions or behavior.
# Example:
def decorator_class(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"{cls.__name__} class decorated")
    return NewClass

@decorator_class
class MyClass:
    def __init__(self):
        print("Original MyClass created")

instance = MyClass()

# Here, the MyClass is wrapped by decorator_class, which modifies or enhances the behavior of the class.

# 3. Creating and Using Context Managers
# A context manager is a way to allocate and release resources properly. The most common way to create context managers is using the with statement, which guarantees that certain cleanup operations are performed after the execution of a block of code.

# Example with Files:
with open('sample.txt', 'w') as file:
    file.write('Hello, World!')
# The file is automatically closed after the block
# In this example, open() acts as a context manager, ensuring the file is closed once the block is exited, even if exceptions occur.

# Custom Context Managers
# You can create custom context managers using:

# The contextlib module.
# Implementing the __enter__ and __exit__ methods in a class.
# Using contextlib:
from contextlib import contextmanager
@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    try:
        yield f
    finally:
        f.close()

with open_file('sample.txt', 'w') as f:
    f.write('Hello, World!')

# Using __enter__ and __exit__:
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileManager('sample.txt', 'w') as f:
    f.write('Hello, World!')

# In both cases, the context manager ensures that resources (like file handles) are properly managed.

# Summary:
# Function Decorators: Useful for modifying the behavior of functions without altering their actual code.
# Class Decorators: Modify or enhance class behavior.
# Context Managers: Ensure resources are properly managed, especially useful for file operations, database connections, and locks.
# Let me know if you'd like to explore any of these topics in more detail!