# syntax
# mapped_object = map(function_name, iterable)
# works as a filtered object -> mapped_object consumed only once second time it is empty 
# map() is a higher order function as it takes another function as a parameter 
# function_name -> name of function to perform operations 
# iterable -> list sequence like string, list tuple, set
#

names = ['Nitin', 'Sanjay', 'Kundan', 'Amit']

def find_lenght(name):
    return name, len(name)

mapper_obj = map(find_lenght, names)
for ele in mapper_obj: 
    print(ele[0], '---> ', ele[1])
print(list(mapper_obj)) # mapper_obj is now empty as filtered object 
print(type(mapper_obj))