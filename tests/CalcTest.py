__author__ = 'Alex'
import unittest
from src import Calculate
calc = Calculate.Calc
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

if __name__ == '__main__':
    unittest.main()