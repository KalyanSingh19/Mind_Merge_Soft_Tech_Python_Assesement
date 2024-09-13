def add_without_arithmetic(a, b):
  while b != 0:
    carry = a & b
    a = a ^ b
    b = carry << 1
  return a

add = add_without_arithmetic(10,20)
print(add)