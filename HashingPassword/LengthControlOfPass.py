import hashlib

while True:
    pas = input("Create Password: ")

    if len(pas) < 8:
        print("Password must have at least 8 characters! Try Again.\n")
    else:
        break

hashpas = hashlib.sha256(pas.encode()).hexdigest()
print("Password Created Successfully\n")

i = 1

while i <= 3:
    npass = input("Enter Password ~ ")

    if len(npass) < 8:
        print("Password must have at least 8 characters! Try Again.\n")
        continue

    if hashpas == hashlib.sha256(npass.encode()).hexdigest():
        print("Logged in Successfully!")
        break
    else:
        print("Incorrect Password!")
        i += 1

if i > 3:
    print("Account Temporarily Locked!")