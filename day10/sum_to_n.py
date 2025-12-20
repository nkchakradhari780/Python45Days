num = int(input("Enter the number: "))

def sumToN(num):
    if num == 0: 
        return 0
    if num == 1:
        return 1
    else:
        sum = num + sumToN(num-1)
        return sum
    
sum = sumToN(num)
print("The sum to the number is: ", sum)
