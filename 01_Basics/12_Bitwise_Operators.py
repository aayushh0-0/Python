# Bitwise Operators in Python
# --------------------------
# Bitwise operators work directly on the binary representation
# of integers.
#
# Operators:
# &   -> Bitwise AND
# |   -> Bitwise OR
# ^   -> Bitwise XOR
# ~   -> Bitwise NOT
# <<  -> Left Shift
# >>  -> Right Shift


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


print("\n----- Bitwise Operators -----")

# Display the binary representation of both numbers
print("Binary of a :", bin(a))
print("Binary of b :", bin(b))


# ---------------- BITWISE AND ----------------

# A bit becomes 1 only when BOTH corresponding bits are 1.
print("a & b  =", a & b)


# ---------------- BITWISE OR ----------------

# A bit becomes 1 when AT LEAST ONE corresponding bit is 1.
print("a | b  =", a | b)


# ---------------- BITWISE XOR ----------------

# A bit becomes 1 when the corresponding bits are DIFFERENT.
print("a ^ b  =", a ^ b)


# ---------------- BITWISE NOT ----------------

# Flips all the bits of a number.
print("~a     =", ~a)


# ---------------- LEFT SHIFT ----------------

# Shifts the bits of a to the left by 1 position.
# For positive integers, this is equivalent to multiplying by 2.
print("a << 1 =", a << 1)


# ---------------- RIGHT SHIFT ----------------

# Shifts the bits of a to the right by 1 position.
# For positive integers, this is equivalent to integer division by 2.
print("a >> 1 =", a >> 1)