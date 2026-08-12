a=int(input("Enter a Number ~ "))
count=0
while a>0:
    count+=1
    a//=10
print(f"Number of Digit is ~ {count}")