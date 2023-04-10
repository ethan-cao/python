
try:
  result = 2 / 0
except EOFError:
  print("EOFErrorEOFError")
except ZeroDivisionError:
  print("ZeroDivisionError")
except:
  # handle all un-caught exceptions
  print("Error")
else:
  # when no exception raised
  print('valid operation')
finally: 
  # executed in any case
  print('called in finally')

  

try:
  raise Exception("An error")
except Exception as error:
  print(error)


