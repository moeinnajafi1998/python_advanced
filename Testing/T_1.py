# 1. Writing Tests with unittest and pytest
# unittest:
# Python’s built-in testing framework.
# It provides a way to create test cases, test suites, and test runners.
# Example of unittest:
import unittest
def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()

# pytest:
# A more flexible and powerful testing framework.
# Supports fixtures, parameterized testing, and has a more readable syntax.
# Example of pytest:
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

# To run tests in pytest, simply run:
# pytest test_file.py
# 2. Mocking and Patching
# Mocking is used to replace parts of your system under test and make assertions about how they were used.

# Using unittest.mock:
from unittest.mock import MagicMock
def fetch_data():
    # Imagine this function makes a network call
    pass

def process_data():
    data = fetch_data()
    return data + " processed"

def test_process_data(mocker):
    mocker.patch('__main__.fetch_data', return_value="mocked data")
    result = process_data()
    assert result == "mocked data processed"

# 3. Debugging with pdb and Other Debugging Tools
# pdb (Python Debugger):

# A built-in interactive debugger for Python.
# You can set breakpoints, step through code, and inspect variables.
# Example of using pdb:
import pdb
def faulty_function(a, b):
    pdb.set_trace()  # Set a breakpoint
    return a / b

faulty_function(1, 0)  # This will raise a ZeroDivisionError

# Other Debugging Tools
# IDE Debuggers: Many IDEs (like PyCharm or VSCode) come with built-in debugging tools that provide a graphical interface for debugging.

# logging module: For debugging purposes, logging can be a great alternative to using print statements.
import logging
logging.basicConfig(level=logging.DEBUG)
def add(a, b):
    logging.debug(f'Adding {a} and {b}')
    return a + b
add(1, 2)

# Third-party Libraries: Tools like pdb++ or ipdb offer enhanced features over the standard pdb.

# Summary
# Testing can be accomplished with unittest and pytest, with pytest being more user-friendly and powerful.
# Mocking allows you to isolate tests from dependencies, using tools like unittest.mock.
# Debugging can be done with pdb or other debugging tools to step through and inspect your code.