a=int(input("Enter a Number ~ "))
sum=0
while a>0:
    temp=a%10
    sum+=temp
    a//=10
print(f"Sum of Digits is ~ {sum}")