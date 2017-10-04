__author__ = 'Alex'
import __main__
main = __main__
class Calc:
    def __init__(self, input1, input2):
        self.input1 = float(input1)
        self.input2 = float(input2)

    def addition(self):
        return round(self.input1 + self.input2, 6)

    def subtraction(self):
        return round(self.input1 - self.input2, 6)

    def multiplication(self):
        return round(self.input1 * self.input2, 6)

    def division(self):
        try:
            return round(self.input1 / self.input2, 6)
        except ZeroDivisionError:
            print("You cannot divide by 0... -_- Try again!")
            return main.main()

#------------methods to call basic operations?________________
    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass
