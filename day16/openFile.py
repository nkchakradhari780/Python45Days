# Opening a file in python
# syntax
# f = open(filename, mode='r',buffering,encoding=None,errors=None,newline=None,closefd=True)
# it consists defafult values so the simple syntax is 
# f = open(filename, mode='r')  

f = open('hello.txt','r')
if f:
    print("file successffully open")

print(type(f))
