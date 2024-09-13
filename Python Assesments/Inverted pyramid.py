def print_right_inverted_half_pyramid(rows):

  for i in range(rows, 0, -1):
    for j in range(i):
      print("*", end="")
    print()


rows = int(input("Enter the number of rows: "))
print_right_inverted_half_pyramid(rows)