# Sequence of Characters 
# immutable 
# Negative indexing is allowed 

name1 = 'Nitin Chakradhari'
name2 = "Nkchakradhari"
name3 = '''Hari Kisan 
Chakradhari'''                  # Multi line string


print(name1)
print(name2)
print(name3)

print(name3[-1])

for i in name3:
    print(i)

# using list comprehension 
list = [char for char in name2]
for i in list:
    print(i)


print(len(name3))

# finding a char or substring 
print(name1.find("k"))  # prints the first occurence index of the char or substring or -1

# slicing a string 
str = name1[:4]     # from starting 
print(str)

str2 = name2[3:]  # to the end
print(str2)

str3 = name2[-3:]  # from -3 index to end
print(str3)

str4 = name3[:-5] # from starting to -5 index
print(str4)

str5 = name1[3:6] 
print(str5)


