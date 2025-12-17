colors = ("red", "yellow", "green")
#          -3/0    -2/1     -1/2

#single item tuple
fruit = ("apple",)
fruit1 = tuple("Apple")

#check type of tuple
print(type(colors))
print(type(fruit1))

print(len(colors))


# accessing items in tuple 
print(colors[1])

#negative indexing 
print(colors[-2])

#range indexing 
print(colors[0:3])
print(colors[-2:])
print(colors[:-2])


more_colors = ("blue", "brown")

colors = colors + more_colors
print(colors)

# unpackeing a tuple 
color1, color2, color3, color4, color5= colors

print(color1)
print(color2)
print(color3)
print(color4)
print(color5)