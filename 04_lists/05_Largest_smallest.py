# Original list
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -1]

# Initialize smallest and largest values
s = float('inf')
l = float('-inf')

# Traverse the list
for i in li:

    # Update largest element
    if i > l:
        l = i

    # Update smallest element
    if i < s:
        s = i

# Display results
print("Largest is ~", l)
print("Smallest is ~", s)