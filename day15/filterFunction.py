# used to filter out the elements of iterable 
# filter(fuction_name, iterable)
# filter object returned can be used only once 

numbers = [67,89,91,34,55,45,46,78]

even_object = filter(lambda n: n % 2 == 0 , numbers)
print(type(even_object))
print(list(even_object))