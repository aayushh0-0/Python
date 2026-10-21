import hashlib
from getpass import getpass
pas=getpass("Enter Number : ")
print("Password Saved!!")
hashpas=hashlib.sha256(pas.encode()).hexdigest()

print("Password is ~ ",pas)
