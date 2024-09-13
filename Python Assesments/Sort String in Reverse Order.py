def sort_reverse(arr):

  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] < arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr
elements = list(map(int, input("Enter the elements of the list: ").split()))
sorted_list = sort_reverse(elements)
print("Sorted list in reverse order:", sorted_list)