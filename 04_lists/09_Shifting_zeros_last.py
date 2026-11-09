# Original list
li = [0, 1, 0, 2, 3, 4, 0, 5, 6]

l = 0  # Position for the next non-zero element

# Traverse the list
for r in range(len(li)):

    # Move non-zero elements towards the left
    if li[r] != 0:
        li[l], li[r] = li[r], li[l]
        l += 1

# Display the modified list
print(li)