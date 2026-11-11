li = [1, 2, 3, 4, 5, 7, 8, 9, 10]
sum = sum(li)
maxnum = max(li)
exsum = 0
for i in range(1, maxnum + 1):
    exsum += i
print("Missing Number is ~ ", exsum - sum)
