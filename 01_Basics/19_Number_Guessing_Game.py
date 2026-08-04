import random
low=int(input("Enter the Lower Limit ~ "))
high=int(input("Enter the Higher Limit ~ "))
tar=random.randint(low,high)
attempts=1
while True:
    a=int(input("Enter the Target ~ "))
    if a>tar:
        print("Too High")
        attempts+=1
    elif a<tar:
        print("Too low")
        attempts+=1
    else:
        print(f"Congratulations..!!! You Got it right in {attempts} attempts")
        break
        
