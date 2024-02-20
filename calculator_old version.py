#old version
    
while (True):
    try:
        print("[+] - addition\n[-] - subtraction\n[*] - multiplication\n[/] - division\n")
        operation = input("Select operation: ")
    except ValueError:
        print("Only symbols are allowed.\n")
        continue

    match operation:
        case '+':
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            result = value1 + value2
            print(f"Result: {result}\n")

        case '-':
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            result = value1 - value2
            print(f"Result: {result}\n")

        case '*':
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            result = value1 * value2
            print(f"Result: {result}\n")

        case '/':
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            result = value1 / value2
            print(f"Result: {result}\n")

        case other:
            print("Wrong choice.\n")
