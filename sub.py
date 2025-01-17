print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

option = int(input("Choose an operation: "))

if option in [1, 2, 3, 4]:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))  

    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    elif option == 4:
        if num2 != 0:  
            result = num1 / num2  
        else:
            print("Error: Division by zero is not allowed.")
            result = None  
else:
    print("Invalid operation entered")
    result = None  # Set result to None if an invalid option is chosen

if result is not None:  # Only print the result if it's valid
    print("The result of the operation is {}".format(result))