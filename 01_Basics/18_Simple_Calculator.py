a=int(input("Enter A : "))
choice=input("Enter Operation (+,-,/,*,%) : ")[0] #Used to Get only one Character from the user even if given a String
b=int(input("Enter B : "))
if choice=='+':
    print(f"Addition is : {a+b}")
elif choice=='-':
    print(f"Difference is : {a-b}")
elif choice=='*':
    print(f"Multiplication is : {a*b}")
elif choice=='/':
    print(f"Division is :{a/b}")
elif choice=='%':
    print(f"Remainder is :{a%b}")
else:
    print(f"--> Invalid Choice <--")
