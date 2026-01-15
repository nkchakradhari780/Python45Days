# for converting characters to upper case 
str1 = "new yourk"

str2 = str1.upper()
print(str2)

# for converting characters to lower case 
str3 = str2.lower()
print(str3)

# for capatalizing the first character of the string 
str4 = str3.capitalize()
print(str4)

# for stripping/removing any trailing white spaces
str1 = "       Hello Nkchakradhari     "
str2 = str1.strip()
print(str2)

# replacing sub string 
str1 = "Hello world, what a beautifull world this is "
print(str1.replace("world", "earth", 1))
print(str1.replace("world", "earth"))

#split the string into a list of sub strings 
fruits = "Apple Banana Kiwi Chery Mango Gwawa"
fruitList = fruits.split()
print(fruitList)

Names = "Nitin,Sanjay,Amit,Komal,Ekta,Isha,Damin"
NameList = Names.split(",",2)       # split by , and upto 2 splits 
print(NameList)