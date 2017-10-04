__author__ = 'Alex'
#imports Calculate class and initiates constructor
from src import Calculate
math = Calculate.Calc
#main with simple loop. while true it does stuff and when false it doesnt
#gets input and splits into three variables then passes second variable to the get_decision() method
def main():
        try:
            math.input1,uInput,math.input2 = input("Enter in some maths: ").split(" ")
            math.input1 = float(math.input1)
            math.input2 = float(math.input2)
            if uInput == "+":
                print(math.addition(math))
            elif uInput == "-":
                print(math.subtraction(math))
            elif uInput == "*":
                print(math.multiplication(math))
            elif uInput == "/":
                print(math.division(math))
            else:
                print("Incorrect operator. Please use one of the following: ")
                main()

        except ValueError:
            print("Incorrect Format, Please enter in correct format. E.G: '# + #'.")
            main()

#runs main
if __name__=='__main__':
    main()
