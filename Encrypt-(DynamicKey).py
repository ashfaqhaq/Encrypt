from tkinter import filedialog
from tkinter import *
from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# you can give input as password too
print("Please provide a password to encrypt the file.")
p1=input()
p1=str(p1)
print("\n\n"+p1+'\n please remember it as it will be used to decrypt the file. ')
password_provided=p1
#password_provided = "Ashfaq" # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes

salt = b'e\r\x84d\x11)C\x01\x90P\xee\xd6\xdd\xf4\xf3_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
     )
key = base64.urlsafe_b64encode(kdf.derive(password))
kfile='Keyfile.txt'
with open(kfile, 'wb') as f:
	f.write(key)
print(key)

input_file = 'input.txt'
output_file = 'input.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

print("The file has been successfully generated.")
print("Would you like to Email the Encrypted file to your friend")
print("1 . Yes")
print("2 . No")
opt=int(input())
if opt==2:
	print("Thanks for encrypting the data.")
