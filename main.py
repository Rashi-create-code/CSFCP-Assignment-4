# calculator.py
def calc():
    while True:
        num1 = input("Num1: ")
        if num1.replace('.', '', 1).isdigit():
            a = float(num1)
            break
        print("Enter a valid number.")

    op = input("Operator (+,-,*,/): ")
    if op not in ["+", "-", "*", "/"]:
        print("Invalid operator")
        return

    while True:
        num2 = input("Num2: ")
        if num2.replace('.', '', 1).isdigit():
            b = float(num2)
            break
        print("Enter a valid number.")

    print("\n--- RESULT ---")
    if op == "+": print(f"{a} + {b} = {a+b}")
    elif op == "-": print(f"{a} - {b} = {a-b}")
    elif op == "*": print(f"{a} * {b} = {a*b}")
    elif op == "/":
        print(f"{a} / {b} = {a/b}" if b != 0 else "Cannot divide by zero")

# Loop wrapper
if __name__ == "__main__":
    while True:
        calc()
        again = input("\nDo another calculation? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break
