
s = "My name is Ayush ~ "

# Split the string into a list of words using whitespace
print(s.split())

# Split the string wherever the character 'i' occurs
print(s.split("i"))

# Store the split words in a new list
snew = s.split()

# Join all words using an underscore as a separator
print("_".join(snew))

# Join list elements using " - " as a separator
print(" - ".join(["python", "java", "C"]))

# Divide the string into three parts around the first occurrence of "is"
print(s.partition("is"))

# Convert the first character of each word into uppercase
print(s.title())

# Swap the case of every alphabetic character
# Uppercase becomes lowercase and lowercase becomes uppercase
print(s.swapcase())
