# key value pair 
# ordered 
# mutable 
# un-indexed
# duplicate kyes not allowed
# Any datatype allowed 

phones = {
    "John" : 33333333,
    "Riya"  : 44444444,
    "Joy": 3333338484
}

print(type(phones))

print(len(phones))

# accessing dictionary items 
print(phones["John"])
print(phones.get("Joy"))

# printing keys 
print(phones.keys())

# update values in dict
phones["John"] = 77744832
print(phones["John"])

# adding element to dictioinay 
phones["Kia"] = 83028322
print(phones)

# updating/ adding dictionary 

more_phones = {
    "Kia" :  23453432,
    "Jordan": 92383489
}

phones.update(more_phones)
print(phones)

# remove element from dict 
phones.pop("John")
print(phones)

phones.popitem() # removes the last item of the dictionary
print(phones)

# phones.clear() # clear the dictionary
# print(phones)

for x in phones:
    print(x)
    print(phones[x])

# printing as item
for x in phones.items():
    print(x)

# printing a saperate key values 
for x, y in phones.items():
    print(x,y)

# nested dictionary
phones_area = {
    "Area1" : {
        "a": 2,
        "b": 3,
        "c": 1,
    },
    "Area2": {
        "d": 4,
        "e": 5,
        "f": 6
    }
}

print(phones_area["Area1"]["a"])