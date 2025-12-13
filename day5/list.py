# lists
# mutable 
# can have duplicate values 

fruits = ["apple", "mango", "banana", "cherry"]
#           -4/0    -3/1      -2/2       -1/3

print(fruits)
print(len(fruits))
print(type(fruits))

# checking if an item present in a list 

if "banana" in fruits:
    print("banana is present in the list")

if "kiwi" not in fruits:
    print("kiwi is not in the fruits")


print(fruits[3]) # indexed access 

print(fruits[-1])   # minus indexing 

print(fruits[0:3])   # getting sub list 

print(fruits[-3:-1])  # minus indexed sub list 

fruits.append("kiwi")       # add item at last of the list 

fruits.insert(2, "kiwi")    # add item at any index

more_fruits = ["papaya", "gwawa"]   # add list at last of the list 

fruits.extend(more_fruits)

print(fruits)

# removing items from list 

fruits.remove("banana")    # remove any items from the list 
print(fruits)

fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)


# cange item in a list 

fruits[0] = "mango_changed"
print(fruits)

fruits[1:3] = ["kiwi_changed", "cherry_changed"]
print(fruits)