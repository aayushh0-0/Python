
# Take a string as input and remove leading/trailing whitespace
s = input("Enter a string ~ ").strip()

# String case conversion
print(s.upper())       # Converts all characters to uppercase
print(s.capitalize())  # Uppercases the first character and lowercases the rest
print(s.lower())       # Converts all characters to lowercase

# Display the cleaned string
print(s)               # Leading and trailing whitespace has been removed

# Replace a specified substring with another substring
old = input("Enter the substring to replace ~ ")
new = input("Enter the replacement substring ~ ")
print(s.replace(old, new))  # Returns a new string with all matches replaced

# Count occurrences of a character or substring
target = input("Enter the character or substring to count ~ ")
print(s.count(target))      # Returns the number of non-overlapping occurrences

# Find the first occurrence of "python" (case-insensitive)
print(s.lower().find("python"))  # Returns the starting index, or -1 if absent

# Replace all spaces with underscores
print(s.replace(" ", "_"))  # Replaces every space with an underscore
