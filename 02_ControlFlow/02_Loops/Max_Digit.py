a=int(input("Enter a Number ~ "))
maxdig=0
while a>0:
    temp=a%10
    maxdig=max(maxdig,temp)
    a//=10
print(f"Maximum Digit in a Number is ~ {maxdig}")