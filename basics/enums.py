from enum import Enum

# enum can be used to create constant

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)        # Color.RED
print(Color.RED.value)  # 1
print(Color.RED.name)   # 'RED'
print(Color["RED"].name)   # 'RED'


print("count: \n", len(Color))   # 3
print("list all enums: \n",  list(Color))

for color in Color:
    print(color)
