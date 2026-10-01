# Create a Calculator class with add, subtract, multiply, and divide methods.
# The divide method should raise a ValueError if dividing by zero.

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        return a / b