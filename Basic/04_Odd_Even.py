a=int(input("Enter a Number : "))

# Way 1 ~ 

if a%2==0:
    print(f"{a} is Even Number")
else:
    print(f"{a} is Odd Number")

    
# Way 2 ~

if a&1==0:
    print(f"{a} is Even Number")
else:
    print(f"{a} is Odd Number")



# Way 3 ~

if a|1>a:
    print(f"{a} is Even Number")
else:
    print(f"{a} is Odd Number")



# Way 4 ~

if (a^1)==a+1:
    print(f"{a} is Even Number")
else:
    print(f"{a} is Odd Number")



# Way 5 ~ Python Special
q,r=divmod(a,2)     #the assigning is as follows the Quotient from the divmod goes to ~ Q & the Remainder goes to R
if r==0:
    print(f"{a} is Even Number")
else:
    print(f"{a} is Odd Number")
