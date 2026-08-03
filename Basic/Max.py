n=int(input("Enter the Size : "))
arr=[]
print("Enter Elements in Array")
for i in range(n):
    a=int(input())
    arr.append(a)
print("Array is ~ ",arr)
print("Maximum Number is ~ ",max(arr))
