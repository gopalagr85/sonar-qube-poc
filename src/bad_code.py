"""Bad code example"""

class Calculator:
    """Calculator class with quality issues"""

    def add(self, x, y):
        # no docstring, unused variables
        a = 10
        b = 20
        if a == 10 and b == 20:
            print("Adding numbers")  # unnecessary print
        return x + y

    def subtract(self, x, y):
        # poor formatting, empty except block
        try:
            result = x - y
        except:
            pass
        return x - y

    def divide(self, x, y):
        # division by zero not handled properly
        return x / y

