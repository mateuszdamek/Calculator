#latest version

while(True):
    try:
        value1 = float(input("Enter first number: "))
        what_to_do = input("Operation (+, -, *, /): ")
        value2 = float(input("Enter second number: "))
    except ValueError:
        print("Input error.")
        continue

    def calculate_result(first, operation, second):
        if(operation == '+'):
            return first + second
        elif(operation == '-'):
            return first - second
        elif(operation == '*'):
            return first * second
        elif(operation == '/'):
            return first / second
        else:
            print("Wrong sign.")

    print(f"Result: {calculate_result(value1, what_to_do, value2)}")




