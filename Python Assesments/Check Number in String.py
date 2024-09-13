def is_numeric(string):
  for char in string:
    if not char.isdigit():
      return False
  return True


string = input("Enter a string: ")
if is_numeric(string):
  print("The string contains only numbers.")
else:
  print("The string contains non-numeric characters.")