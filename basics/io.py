import datetime

birth_year = input("Enter your birth year:")
current_year = datetime.datetime.now().year
age = current_year - int(birth_year)
print("age is: ", age)


fileName = "test.txt"
with open(fileName, 'r') as file:
  content = file.read()
  print(content)