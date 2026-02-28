"""Good code example"""

class Calculator:
    """A simple calculator class"""

    def add(self, x, y):
        """Return the sum of x and y"""
        return x + y

    def subtract(self, x, y):
        """Return the difference between x and y"""
        return x - y

    def divide(self, x, y):
        """Return the division result, handle division by zero"""
        if y == 0:
            return None
        return x / y


def main():
    """Main function"""
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.subtract(10, 7))
    print(calc.divide(8, 2))


if __name__ == "__main__":
    main()
