a=int(input("Enter a Number : "))

"""Here i Will be Demonstrating the 4 Ways of Getting the Even Odd"""

# Way ~ 1
if a%2==0:
    print("Number is Even")
else:
    print("Number is Odd")

#Way ~ 2 
if a&1==0:
    print("Number is Even")
else:
    print("Number is Odd")

#Way ~ 3
if a|1>a:
    print("Number is Even")
else:
    print("Number is Odd")

#Way ~ 4
q,r=divmod(a,2)
if r==0:
    print("Number is Even")
else:
    print("Number is Odd")
