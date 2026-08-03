import random
secret=random.randint(1,100)
attempts=0
while True :
    guess=int(input("Enter your Guess : "))
    attempts+=1
    if guess>secret:
        print("Too High")

    elif guess<secret:
        print("Too Low")
    else:
        print("Congratulations,You guessed it Right!!")
        print(f"You guessed it in {attempts} attempts")
        break
