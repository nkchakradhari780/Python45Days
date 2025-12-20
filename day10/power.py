num = int(input("Enter a number to get power: "))
pow = int(input("Enter the power: "))

def powerToN(num, pow):
    if pow == 0:
        return 1
    else: 
        power = num * powerToN(num,pow-1)
        return power

powerTopow = powerToN(num, pow)

print("The power to n is ", powerTopow)