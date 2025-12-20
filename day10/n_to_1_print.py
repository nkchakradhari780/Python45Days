num = int(input("Enter the number n: "))

def printToOne(num):
    if num == 0:
        print(0)
    elif num == 1:
        print(1)
    else: 
        print(num)
        printToOne(num-1)

printToOne(num)