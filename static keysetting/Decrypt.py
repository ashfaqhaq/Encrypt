import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys

password_provided = "Ashfaq" # This is input in the form of a string
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


def flow():
	input_file = 'test.encrypted'
	output_file = 'output.txt'

	with open(input_file, 'rb') as f:
   		data = f.read()

	fernet = Fernet(key)
	encrypted = fernet.decrypt(data)

	with open(output_file, 'wb') as f:
   		f.write(encrypted)
	print("The file has been decrypted")    


def GetPass():

	print("Enter the Password for decryption")
	p=input()
	pas = p.encode() # Convert to type bytes

	salt = b'e\r\x84d\x11)C\x01\x90P\xee\xd6\xdd\xf4\xf3_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
	kdf = PBKDF2HMAC(
    	algorithm=hashes.SHA256(),
    	length=32,
    	salt=salt,
    	iterations=100000,
    	backend=default_backend()
    	)
	p1= base64.urlsafe_b64encode(kdf.derive(pas))
	if (p1!=key):
		print("Sorry "+ str(n) +" ,but the password is incorrect.")
		print("Re-Enter the password")
		GetPass()
	elif(p1==key):
		print('The password is correct.')	
		flow()

print("Enter your Name:")
n=input()
GetPass()			
			

