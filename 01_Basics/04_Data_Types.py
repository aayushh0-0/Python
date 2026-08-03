"""
==========================================================
Program : Data Types in Python
==========================================================
"""

print("========== INTEGER ==========")
age = 19
print("Value :", age)
print("Type  :", type(age))


print("\n========== FLOAT ==========")
height = 5.10
print("Value :", height)
print("Type  :", type(height))


print("\n========== STRING ==========")
name = "Ayush"
print("Value :", name)
print("Type  :", type(name))


print("\n========== BOOLEAN ==========")
is_student = True
print("Value :", is_student)
print("Type  :", type(is_student))


print("\n========== LIST ==========")
fruits = ["Apple", "Mango", "Banana"]
print("Value :", fruits)
print("Type  :", type(fruits))

# Lists are mutable
fruits.append("Orange")
print("After Append :", fruits)


print("\n========== TUPLE ==========")
coordinates = (10, 20)
print("Value :", coordinates)
print("Type  :", type(coordinates))

# Tuples are immutable
# coordinates[0] = 100   # This will produce an error


print("\n========== SET ==========")
numbers = {10, 20, 30, 40, 10}
print("Value :", numbers)
print("Type  :", type(numbers))
print("Note  : Duplicate values are removed automatically.")


print("\n========== DICTIONARY ==========")
student = {
    "Name": "Ayush",
    "Age": 19,
    "College": "GL Bajaj"
}

print("Value :", student)
print("Type  :", type(student))


print("\n========== NONE TYPE ==========")
value = None
print("Value :", value)
print("Type  :", type(value))


print("\n========== TYPE CHECKING ==========")
print(type(100))
print(type(99.99))
print(type("Python"))
print(type(False))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({"Name": "Ayush"}))
print(type(None))


print("\n========== MUTABLE vs IMMUTABLE ==========")

# Mutable Example
my_list = [1, 2, 3]
print("Original List :", my_list)

my_list.append(4)
print("Modified List :", my_list)

# Immutable Example
my_tuple = (1, 2, 3)
print("Tuple :", my_tuple)

# my_tuple.append(4)   # Error


print("\n========== SUMMARY ==========")

print("int        -> Whole Numbers")
print("float      -> Decimal Numbers")
print("str        -> Text")
print("bool       -> True / False")
print("list       -> Ordered & Mutable")
print("tuple      -> Ordered & Immutable")
print("set        -> Unordered & Unique Elements")
print("dict       -> Key-Value Pairs")
print("NoneType   -> Represents No Value")