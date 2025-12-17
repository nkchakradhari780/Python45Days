# taking a particluar elements from the list 
fruits = ["apple", "mango", "banana", "kiwi", "papaya", "cherry"]

new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

#copy a list 
new_fruits1 = fruits.copy()
print(new_fruits1)

# list concatenation 
new_fruits2 = fruits + new_fruits
print(new_fruits2)

