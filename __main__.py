__author__ = 'Alex'
from src import Calculate, UI
def main():
    math = Calculate.Calc

    math.input1 = float(input("Enter in a number: "))
    math.input2 = float(input("Enter in another number: "))

if __name__=='__main__':
    main()
