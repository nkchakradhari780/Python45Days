number = int(input("Enter a number to find factorial: "))

def factorialNumber(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1        
    else: 
        return num * factorialNumber(num-1)
    
factNumber = factorialNumber(number)

print("Factorial of Number is: ", factNumber)