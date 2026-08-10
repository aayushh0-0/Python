# Create a list object and make 'a' refer to it
a = [10, 20, 30]

# 'b' is assigned to 'a'
# This does NOT create a new list.
# Both 'a' and 'b' refer to the SAME list object.
b = a

# This creates a completely NEW list object.
# It has the same values as 'a', but it is a different object.
c = [10, 20, 30]


# '==' checks whether the VALUES/CONTENTS are equal.
# a and b contain the same values → True
print("a == b :", a == b)

# 'is' checks whether both variables refer to the SAME OBJECT.
# a and b refer to the same list → True
print("a is b :", a is b)


# a and c contain the same values → True
# Even though they are different list objects.
print("a == c :", a == c)

# a and c are DIFFERENT list objects → False
print("a is c :", a is c)


# 'is not' is the opposite of 'is'.
# Since a and c are different objects → True
print("a is not c :", a is not c)