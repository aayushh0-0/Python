"""
~ Displays the Hashing of the Password i.e. the One way Hashing ~

"""

import hashlib  # Library used for Hashing
pas=input("Enter a Password : ")
hashpas=hashlib.sha256(pas.encode()).hexdigest() 
#Encode is Used for Encoding the Pass i.e converting the pass string intoo bytes  
#Hexdigest is Used to Convert the hash into Hexdecimal String
print()
print("Original Password ~ ",pas)
print()
print("Hashed Password ~ ",hashpas)
