from tkinter import filedialog
from tkinter import *
from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# you can give input as password too
# p=input()
# password_provided=p
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
kfile='Keyfile.txt'
with open(kfile, 'wb') as f:
	f.write(key)
print(key)

input_file = 'test.txt'
output_file = 'test.encrypted'

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


# key = Fernet.generate_key()
# to open a file
'''def show():
	i1="Take input from console and encrypt input."
	i2="Take input from console and save the txt file."
	o1="give output generated in console."
	o2="give output in txt file."
	print(i1+"\n"+i2+"\n"+o1+"\n"+o2+"\n")
# def one():
print("Please provide the mesage to be ecoded ")
message="hello fraand chai peelo"

encoded=message.encode()
# key = Fernet.generate_key()
print(key)
f=Fernet(key)
encrypted=f.encrypt(encoded)
print(encrypted)
f2=Fernet(key)
Original=f2.decrypt(encrypted)	
print(Original)






class En:
	def encode():
		print("Please provide the mesage to be ecoded ")
		message="hello fraand chai peelo"
		encoded=message.encode()
		key = Fernet.generate_key()
		print(key)
		f=Fernet(key)
		encrypted=f.encrypt(encoded)
		print(encrypted)
	def decode(encode):
		f2=Fernet(key)
		Original=f2.decrypt(encrypted)	
		print(Original)
'''		
'''
def encode():
	print("Please provide the mesage to be ecoded ")
	message="hello fraand chai peelo"
	encoded=message.encode()
	# key = Fernet.generate_key()
	print(key)
	f=Fernet(key)
	encrypted=f.encrypt(encoded)
	print(encrypted)
def decode():
	f2=Fernet(key)
	Original=f2.decrypt(encrypted)	
	print(Original)
if __name__ == '__main__':
	# show()
	encode()
	decode()


# def fileopen():
	root = Tk()
	root.filename =filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	print (root.filename)



# generating a key
def encrypt():
	key = Fernet.generate_key()
	file = open('hello', 'wb')
	file.write(key) # The key is type bytes still
	file.close()
	print(key)# printing a key



# saving a file
def filesave():
	root = Tk()
	root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	print (root.filename)
'''