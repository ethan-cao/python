# set is mutable, without duplicated value, not ordered

set1 = {"Tom", "Jack", "Tim"}
set2 = {"Tom", "Alex"}

print("Tom" in set1)

intersect = set1 & set2
print(intersect)

union = set1 | set2
print(union)

difference = set1 - set2
print(difference)

isSuperSet = set1 > set2
print(isSuperSet)
# 
