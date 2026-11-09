l = [1, 2, 3, 4, 5, 1, 1, 2, 3, 4]
uni=[]
for i in l:
    if i not in uni:
        uni.append(i)
print(uni)
