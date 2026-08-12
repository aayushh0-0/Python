a=int(input("Enter a Number ~ "))
rev_num=0
while a>0:
    temp=a%10
    rev_num=rev_num*10+temp
    a//=10
print(f"Reversed Number is ~ {rev_num}")
