__author__ = 'Alex'
#imports unittest and the Calculate file to test
import unittest
from src import Calculate
calc = Calculate.Calc
#testing class that tests all four functions in the Calculate file
class CalcTester(unittest.TestCase):

    def test_addition_in_calculate(self):
        calc.input1 = 5
        calc.input2 = 5
        self.assertEqual(calc.addition(calc), 10)

    def test_subtraction_in_calculate(self):
        calc.input1 = 5
        calc.input2 = 1
        self.assertEqual(calc.subtraction(calc), 4)

    def test_multiplication_in_calculate(self):
        calc.input1 = 3
        calc.input2 = 2.245
        self.assertEqual(calc.multiplication(calc), 6.735)

    def test_division_in_calculate(self):
        calc.input1 = 3
        calc.input2 = 3
        self.assertEqual(calc.division(calc), 1)

#calls the unittest's main method
if __name__ == '__main__':
    unittest.main()