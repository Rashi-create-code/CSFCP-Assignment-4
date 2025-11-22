# calculator.py
def calc():
    while True:
        num1 = input("Num1: ")
        if num1.replace('.', '', 1).isdigit():
            a = float(num1)
            break
        print("Enter a valid number.")

    op = input("Operator (+,-,*,/): ")

    while True:
        num2 = input("Num2: ")
        if num2.replace('.', '', 1).isdigit():
            b = float(num2)
            break
        print("Enter a valid number.")

    if op == "+": print(a+b)
    elif op == "-": print(a-b)
    elif op == "*": print(a*b)
    elif op == "/": print(a/b if b!=0 else "Divide by zero")
    else: print("Unknown operator")

if __name__ == "__main__":
    calc()

