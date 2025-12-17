tuple1 = ('a', 'b', 'c', 'd', 'e')
temp_list =[]

for i in reversed(tuple1):
    temp_list.append(i)

reversed_tuple = tuple(temp_list)

print(reversed_tuple)
print(type(reversed_tuple))
