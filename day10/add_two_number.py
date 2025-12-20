def add(n1, n2):
    print("n1: ", n1)
    print("n2: ", n2)
    sum = n1 + n2
    return sum

x = 1
y = 3

sum = add(x,y)
print("The sum is: ", sum)

# named arguments
print("The sum of named Arguments is : ",add(n2=5, n1=7))


