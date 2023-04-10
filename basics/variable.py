from function import f1

# Python is a dynamically typed language, 
# meaning that the data type of a variable is determined at runtime based on the value assigned to it. 
# This is in contrast to statically typed languages, 
# where the data type of a variable must be explicitly declared before it can be used.


# everything in Python is an object
string1 = 'Python is a programming language'
string2 = "string"

print(string1.find("Python"))  # 0, index of Python
print("Python" in string1)  # True


isOk = True

print("memory location of vaeiable: ", id(isOk))
 
# annotation: specify variable type
n1: int = 2

print(f1(2,5))
