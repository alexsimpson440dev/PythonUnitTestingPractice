__author__ = 'Alex'
from src import Calculate
math = Calculate.Calc
def main():
    while True:
        try:
            math.input1,uInput,math.input2 = input("Enter in some maths: ").split(" ")
            math.input1 = float(math.input1)
            math.input2 = float(math.input2)
            get_decision(uInput)
            return False
        except ValueError:
            print("Incorrect Format, Please enter in correct format. E.G: '# + #'.")



def get_decision(maths):
    add = "+"
    sub = "-"
    mul = "*"
    div = "/"

    if maths == add:
        print(math.addition(math))
    elif maths == sub:
        print(math.subtraction(math))
    elif maths == mul:
        print(math.multiplication(math))
    elif maths == div:
        print(math.division(math))
    else:
        print("Not a valid Calculation, Please try again! Valid Calculations: '+', '-', '/', '*'.")
        main()

if __name__=='__main__':
    main()
