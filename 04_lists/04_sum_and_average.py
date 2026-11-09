# Original list
li = [1, 4, 2, 3, 6, 7, 5, 8]

# Initialize sum
total = 0

# Traverse the list and calculate the sum
for i in li:
    total += i

# Calculate average
avg = total / len(li)

# Display results
print("Sum is:", total)
print("Average is:", avg)