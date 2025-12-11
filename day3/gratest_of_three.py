num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is Greatest")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is Greatest")
else: 
    print(f"{num3} is Greatest")
    