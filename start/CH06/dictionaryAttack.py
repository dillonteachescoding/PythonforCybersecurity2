#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By 

#Import libaries utilized for hashing

from passlib.hash import sha512_crypt

# File paths

ShadowFile = r"/home/justincase/Desktop/IT 102/PythonforCybersecurity2/start/CH06/shadow"

PasswordFile = r"/home/justincase/Desktop/IT 102/PythonforCybersecurity2/start/CH06/top1000.txt"


# Create a function to guess our password

def GuessPassword(ShadowFile, PasswordFile):
    successful_attempts = [] # List to store succesful username password.

    with open(ShadowFile, 'r') as sf, open(PasswordFile, 'r') as pf:
        shadows = sf.readlines()
        passwords = pf.readlines()
        
        for shadow in shadows:
            #Split once and unpack username and password hash
            parts = shadow.split(':')
            if len(parts) < 2 or '!' in parts[1] or '*' in parts[1]:
                continue # Skip the unwanted lines

            Username, HashPassword = parts[0], parts[1].strip()

            for password in passwords:
                password = password.strip()

                    #Attemp to verfiy if the password matches the SHA-512 hash
                try:
                    if sha512_crypt.verify(password, HashPassword):
                        successful_attempts.append((Username, password))
                        break
                except ValueError:
                    continue #Skip in-valid hashes
    #Print only our succesul attempts
    print("Successful Password found:")
    for Username, password in successful_attempts:
        print(Username, password)
# Call the function
GuessPassword(ShadowFile, PasswordFile)

