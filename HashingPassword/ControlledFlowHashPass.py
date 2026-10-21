import hashlib
pas=input("Create Password ~ ")
print("Password Saved Successfully!! \n\n")
hashpass=hashlib.sha256(pas.encode()).hexdigest()
i=1
while i<=3:    
    npass=input("Enter Password : ")
    if hashpass==hashlib.sha256(npass.encode()).hexdigest():
        print("~ Logged in Successfully ~ \n")
        break
    else:
        print("Oops! Incorrect Password, Try Again!!\n")
    if i==3:
        print("Sorry, Account Temporarily Locked due to Multiple Attempts\n")
    i+=1
