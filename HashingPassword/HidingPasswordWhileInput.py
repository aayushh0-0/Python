import hashlib  # Library used for hashing
from getpass import getpass  # Takes password input without displaying characters

pas = getpass("Enter Number: ")  # Takes password input securely

print("Password Saved!!")  # Displays a confirmation message (not actually saved to a file)

# .encode() converts the password string into bytes
# hashlib.sha256() generates a SHA-256 hash of the password
# .hexdigest() converts the hash into a hexadecimal string
hashpas = hashlib.sha256(pas.encode()).hexdigest()

# WARNING: Printing the original password reveals it on the screen
print("Password is ~ ", pas)