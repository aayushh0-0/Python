n=int(input("Enter the Number for Finding the Factorial :  "))
fact=1
for i in range(1,n+1,1):
    fact*=i
print(f"Factorial is ~ {fact}")
