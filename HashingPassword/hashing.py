"""
~ Displays the Hashing of the Password i.e. the One way Hashing ~

"""

import hashlib
pas=input("Enter a Password : ")
hashpas=hashlib.sha256(pas.encode()).hexdigest()
print()
print("Original Password ~ ",pas)
print()
print("Hashed Password ~ ",hashpas)
