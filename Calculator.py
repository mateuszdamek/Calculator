
while (True):
    try:
        print("[1] - addition\n[2] - subtraction\n[3] - multiplication\n[4] - division\n")
        operation = int(input("Select operation: "))
    except ValueError:
        print("Only numbers are allowed.\n")
        continue

    match operation:
        case 1:
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            result = value1 + value2
            print(f"Result: {result}\n")

        case 2:
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            result = value1 - value2
            print(f"Result: {result}\n")

        case 3:
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            result = value1 * value2
            print(f"Result: {result}\n")

        case 4:
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            result = value1 / value2
            print(f"Result: {result}\n")

        case other:
            print("Wrong choice.\n")



