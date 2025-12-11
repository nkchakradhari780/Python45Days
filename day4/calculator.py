num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

operator = input("Enter operator: ")

match operator:
    case "+":
        print("the sum is ", num1 + num2)
    case "-": 
        print("the difference is : ", num1 - num2)
    case "*":
        print("the multiplication is :", num1 * num2)
    case "/":
        print("the divisoin is :", num1/num2)
    case _ :
        print("Enter a valid operator.")
    