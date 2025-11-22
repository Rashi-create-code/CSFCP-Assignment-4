# calculator.py
def calc():
    a = float(input("Num1: "))
    op = input("Operator (+,-,*,/): ")
    b = float(input("Num2: "))
    if op == "+": print(a+b)
    elif op == "-": print(a-b)
    elif op == "*": print(a*b)
    elif op == "/": print(a/b if b!=0 else "Divide by zero")
    else: print("Unknown operator")

if __name__ == "__main__":
    calc()
