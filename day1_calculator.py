num1 = int(input("Enter first number to calcultate: "))
num2 = int(input("Enter second number to calculate: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    sum = num1 + num2
    print("The sum is: ", sum)
elif operator == "-":
    subtaction = num1 - num2
    print("The subtraction is: ", subtaction)
elif operator == "*":
    multiplication = num1 * num2
    print("The multiplication is: ", multiplication)
elif operator == "/":
    if num2 != 0:
        division = num1 / num2
        print("The division is: ", division)
    else: 
        print("Error: Division by zero is not allowed.")
    