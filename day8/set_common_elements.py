ar1 = [1,3,4,5,10,40,80]
ar2 = [7,2,1,40,80]
ar3 = [40,80,32,23,2323,4232]

set1 = set(ar1)
set2 = set(ar2)
set3 = set(ar3)

s1s2 = set1.intersection(set2)
print(s1s2)
s1s2s3 = s1s2.intersection(set3)
print(s1s2s3)

output_list = list(s1s2s3)

print(output_list)
