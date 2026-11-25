def basic_calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Invalid input! Please enter valid numeric values.")
        return

    print("\nSelect Operation: +, -, *, /, %, **")
    op = input("Enter operator: ").strip()

    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '*':
        res = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        res = num1 / num2
    elif op == '%':
        res = num1 % num2
    elif op == '**':
        res = num1 ** num2
    else:
        print("Error: Invalid operation choice.")
        return

    print(f"Result: {num1} {op} {num2} = {res:.2f}")


if __name__ == "__main__":
    basic_calculator()
