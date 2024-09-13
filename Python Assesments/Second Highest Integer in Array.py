def find_second_highest(arr):
  if len(arr) < 2:
    return None

  highest = arr[0]
  second_highest = arr[1]

  for num in arr:
    if num > highest:
      second_highest = highest
      highest = num
    elif num > second_highest and num != highest:
      second_highest = num

  return second_highest

array = list(map(int, input("Enter the elements of the array: ").split()))

second_highest = find_second_highest(array)

# Print the result
if second_highest is not None:
  print("The second highest integer is:", second_highest)
else:
  print("There is no second highest integer in the array")