a=int(input("Enter a Number to Check for Prime Number ~ "))
isprime=True
for i in range(2,a//2): # range(__) alwwys requires an int value
    if a%i==0:
        isprime=False
        break
if isprime:
    print("Prime Number")
else:
    print("Not a Prime Number")