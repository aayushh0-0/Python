
# Initialize an empty dictionary to store character frequencies
frequency = {}

# Accept a string from the user
s = input("Enter a String ~ ")

# Traverse each character in the string
for char in s:

    # Check whether the character already exists in the dictionary
    if char in frequency:

        # If it exists, increment its frequency by 1
        frequency[char] += 1

    else:
        # If it is encountered for the first time, initialize its count to 1
        frequency[char] = 1

# Display the character frequency dictionary
print(frequency)
