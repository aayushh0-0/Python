# Membership Operators in Python
# -----------------------------
# Membership operators are used to check whether
# an element exists inside a sequence or collection.
#
# Python provides two membership operators:
#
# 1. in      -> Checks whether an element is present
# 2. not in  -> Checks whether an element is NOT present


# Create a list of numbers
numbers = [10, 20, 30, 40, 50]

# Create a string
name = "Ayush"


# ---------------- LIST ----------------

# '30 in numbers' checks whether 30 exists in the list.
# Since 30 is present, the result is True.
print("30 in numbers :", 30 in numbers)

# '60 in numbers' checks whether 60 exists in the list.
# Since 60 is NOT present, the result is False.
print("60 in numbers :", 60 in numbers)

# '60 not in numbers' checks whether 60 does NOT exist.
# Since 60 is not present, the result is True.
print("60 not in numbers :", 60 not in numbers)


# ---------------- STRING ----------------

# Check whether the character 'A' exists in the string.
print("'A' in name :", 'A' in name)

# Check whether the character 'z' exists in the string.
print("'z' in name :", 'z' in name)

# We can also check for a complete substring.
# "yush" is present inside "Ayush".
print("'yush' in name :", 'yush' in name)

# Check whether "xyz" is NOT present in the string.
print("'xyz' not in name :", 'xyz' not in name)