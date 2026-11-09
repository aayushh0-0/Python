
# Function to remove a character from a given index
def removenth(s, n):

    # Check whether the given index is invalid
    if n < 0 or n >= len(s):
        return s  # Return the original string if index is invalid

    # Combine the characters before and after the specified index
    return s[:n] + s[n+1:len(s)]


# Call the function and display the modified string
print(removenth("AYUSH", 3))
