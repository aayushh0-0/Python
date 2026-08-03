"""
Program : Type Casting in Python

"""

print("========== IMPLICIT TYPE CASTING ==========")

a = 10          # int
b = 5.5         # float

c = a + b       # int is automatically converted to float

print("Value :", c)
print("Type  :", type(c))


print("\n========== EXPLICIT TYPE CASTING ==========")

# String to Integer
num = "100"
print("\nOriginal :", num, type(num))

num = int(num)
print("After int() :", num, type(num))

# Integer to Float
x = 25
print("\nOriginal :", x, type(x))

x = float(x)
print("After float() :", x, type(x))

# Float to String
y = 99.99
print("\nOriginal :", y, type(y))

y = str(y)
print("After str() :", y, type(y))

# Integer to Boolean
z = 1
print("\nOriginal :", z, type(z))

z = bool(z)
print("After bool() :", z, type(z))