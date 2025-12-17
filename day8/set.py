# unordered
# immutable values
# unindexed
# no duplicate allowed
# mix of any datatype 

names = {"nitin", "sanjay", "komal", "ankita", "isha"}

print(names)

print(len(names))
print(type(names))


# accessing the items in a  set 
for i in names:
    print(i)

if "ankita" in names:
    print("Yes Ankita in set.")

if "ekta" not in names:
    print("Yes Ekta is not in set")

# add new values
names.add("ekta")
print(names)

names_list = {"om", "yash", "khilesh", "nitin"}
names.update(names_list)
print(names)


# removing elements
names.remove("om")
names.discard("yash") #this will not throw error if value is not present 
print(names)

s1 = {'a', 'b', 'c', 'd', 'e'}
s2 = {'f', 'g', 'h', 'a', 'b'}

# joining two sets 
s3 = s1.union(s2)
print(s3)

s1.update(s2)
print(s1)

# keep duplicates only 
s1.intersection_update(s2)
print(s1)


# keep all values except duplicates
s1.symmetric_difference_update(s2)
print(s1)



