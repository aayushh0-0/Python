"""
~ Displays the Hashing of the Password i.e. the One way Hashing ~
"""

import hashlib  # Library used for Hashing

pas = input("Enter a Password : ")
hashpas = hashlib.sha256(pas.encode()).hexdigest()

# Encode is used for encoding the password string into bytes.
# Hexdigest is used to convert the hash into a hexadecimal string.

print()
print("Original Password ~ ", pas)
print()
print("Hashed Password ~ ", hashpas)