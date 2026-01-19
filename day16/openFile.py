# Opening a file in python
# syntax
# f = open(filename, mode='r',buffering,encoding=None,errors=None,newline=None,closefd=True)
# it consists defafult values so the simple syntax is 
# f = open(filename, mode='r')  

f = open('hello.txt','r')
if f:
    print("file successffully open")

print(type(f))

# buffering ->  Positive interger value used to set bugger size for file
# it should be 1 or more than 1 in text mode
# in binary mode buffer size can be 0
# defaudefault buggering size := 4096-8192

# encoding -> encoding type used to decode and encode file
# should be used in text mode only
# default depends on OS 
# for windows cp1252
 
# errors -> represents how encodeing and decoding errors are to be handled
# cannot be used in binary mode 
# some standard values are -> strict, ignore, replace etc.

# newLine -> \n, \r, \r\n