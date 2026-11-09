# Creating two lists
li = [10, -5, 20, -15, 30, -10, 0, 8, -3]
li2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# METHOD 1: Using for loop and membership operator

# Empty list to store common elements
common = []

# Traverse the first list
for i in li:

    # Check if the element exists in the second list
    # Also ensure that duplicates are not added
    if i in li2 and i not in common:
        common.append(i)

# Display common elements
print("Using for loop:", common)


# METHOD 2: Using set intersection (&)

# Convert both lists into sets and find common elements
common = set(li) & set(li2)

# Display the result
print("Using set intersection:", common)


# METHOD 3: Using intersection() method

# Convert lists into sets and use intersection()
common = set(li).intersection(set(li2))

# Display the result
print("Using intersection():", common)