__author__ = 'Alex'

class Calc:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def addition(self):
        return self.input1 + self.input2

    def subtraction(self):
        return self.input1 - self.input2

    def multiplication(self):
        return self.input1 * self.input2

    def division(self):
        return self.input1 / self.input2

#------------methods to call basic operations?________________
    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass
