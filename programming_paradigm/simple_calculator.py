# this is a simple calculator program
class SimpleCalculator:

    def add (self,a,b):
        return a + b

    def subtract (self,a,b):
        return a - b

    def multiply (self,a,b):
        return a * b
    def divide (self, a ,b):

        if b != 0:
            return a / b
        else:
            raise ValueError("Denominator cannot be zero")