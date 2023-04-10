list = [1, 2, 3]

list.append(4)
list.insert(0, -1)
list[0] = -2

print(list)
print(len(list))
print(list[0:3]) 
print(list[0])  
print(list[-1])
print(2 in list)

print("\n------------iteration1-----------")
for item in list:
  print(item)

print("\n------------iteration2-----------\n")
i = 0
while i < len(list):
  print(list[i])
  i += 1


