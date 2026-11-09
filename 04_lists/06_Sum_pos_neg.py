# Original list
li = [10, -5, 20, -15, 30, -10, 0, 8, -3]

# Initialize sums and counters
sumpos = 0
sumneg = 0
pos_count = 0
neg_count = 0
zero_count = 0

# Traverse the list
for i in li:

    if i > 0:
        sumpos += i
        pos_count += 1

    elif i < 0:
        sumneg += i
        neg_count += 1

    else:
        zero_count += 1

# Display results
print("Positive sum:", sumpos)
print("Negative sum:", sumneg)
print("Positive count:", pos_count)
print("Negative count:", neg_count)
print("Zero count:", zero_count)