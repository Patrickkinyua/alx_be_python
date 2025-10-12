class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method:
        Performs addition without needing access to class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method:
        Has access to class attributes through 'cls'.
        Prints the calculation type before performing multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
