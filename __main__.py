__author__ = 'Alex'
from src import Calculate, UI
math = Calculate.Calc
def main():

    math.input1,uInput,math.input2 = input("Enter in some maths: ").split(" ")
    math.input1 = float(math.input1)
    math.input2 = float(math.input2)
    get_decision(uInput)

def get_decision(maths):
    add = "+"
    sub = "-"
    mul = "*"
    div = "/"

    if maths == add:
        print(math.addition(math))
    if maths == sub:
        print(math.subtraction(math))
    if maths == mul:
        print(math.multiplication(math))
    if maths == div:
        print(math.division(math))

if __name__=='__main__':
    main()
