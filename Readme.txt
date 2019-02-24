Project Title : Encrypting and Decrypting Data

IMPORTANT :
	MAKE SURE YOU HAVE THE ALL THE 3 txt FILES IN THE SAME DIRECTORY WHERE THE .py script is present.
	

Important variables and their function:
	<kdf> calculates the hash value of the message over a period of 100k[1 Lakh] iterations,the algorithm used here is SHA256.
	<key> holds the password in the base64 format so that it can be used for encryption and generate a message digest.
	













Before making changes to any code,please ensure that you have the following modules/packages installed.
Step 0:  You will be requiring some modules,out of which one requires installation
	0.1 Installing the modules:
		pip install cryptography
	0.1.E if any error is occured google search the error with the exact keywords
	0.2 Check if the modules are installed: <Go to the Command line or Python idle and type the following>
		import os
		import system
		import cryptography
	0.3.E if any error has occured, then the installation of any of the module hasn't been completed properly	
	0.3 If the intrepreter doesn't return any error then you are set to go.
steap 1: You may replace the variable "salt" by generating a random value from <os.random(16)>
step2 : Make the changes and run the code 