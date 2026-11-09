# Creating a list
num = [1, 2, 3, 4, 5]

# 1. append(): Adds a single element at the end
num.append(0)
print(num)

# 2. extend(): Adds multiple elements at the end
num.extend([10, 20, 30])
print(num)

# 3. insert(): Inserts an element at the specified index
num.insert(1, 23)
print(num)

# 4. remove(): Removes the first occurrence of the given value
num.remove(3)
print(num)

# 5. pop(index): Removes and returns the element at the given index
num.pop(1)
print(num)

# 6. pop(): Removes and returns the last element
num.pop()
print(num)

# 7. index(): Returns the index of the first occurrence of an element
print(num.index(0))

# 8. count(): Returns the number of occurrences of an element
print(num.count(0))

# 9. Membership operator: Checks whether an element exists in the list
print(10 in num)

# 10. reverse(): Reverses the original list
num.reverse()
print(num)

# 11. sorted(): Returns a new sorted list without modifying the original
print(sorted(num))

# Display the original list to verify it remains unchanged by sorted()
print(num)