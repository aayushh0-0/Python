a=int(input("Enter a Number : "))
b=int(input("Enter a Number : "))
c=int(input("Enter a Number : "))
#print(max(a,b,c))
if a>b and a>c:
    print(f"{a} is the Largest")
elif b>a and b>c:
    print(f"{b} is the Largest")
else:
    print(f"{c} is the Largest")
