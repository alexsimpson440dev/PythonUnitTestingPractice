__author__ = 'Alex'
#imports __main__ file and initiates the constructor
import __main__
main = __main__

#Calc class that has two float inputs
#has for methods for calculating based of the users in put in main
class Calc:
    def __init__(self, input1, input2):
        self.input1 = float(input1)
        self.input2 = float(input2)

    def addition(self):
        total = round(self.input1 + self.input2, 6)
        return total

    def subtraction(self):
        total = round(self.input1 - self.input2, 6)
        return total

    def multiplication(self):
        total =  round(self.input1 * self.input2, 6)
        return total

    def division(self):
        try:
            total =  round(self.input1 / self.input2, 6)
            return total
        except ZeroDivisionError:
            error = "Cannot divide by Zero!"
            return error

#------------methods to call basic operations?________________
    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass
