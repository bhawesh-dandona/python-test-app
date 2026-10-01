# Create a Calculator class with add, subtract, multiply, and divide methods.
# The divide method should raise a ValueError if dividing by zero.

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        return a / b

    def modulo(self, a, b):
        """Return the remainder of a divided by b."""
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        return a % b