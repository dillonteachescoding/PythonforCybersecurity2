#Password cracking python script
# Read, write files and create functions 
from passlib.hash import sha256_crypt

#Load the files for shadwon and password list

shadow_file = '/home/justincase/Desktop/IT 102/PythonforCybersecurity2/start/CH04/shadow.txt'
password_list = '/home/justincase/Desktop/IT 102/PythonforCybersecurity2/start/CH04/password.txt'

#Create a function that is going crack passwords
def crack_password(shadow_file, password_list):
    with open(shadow_file, 'r') as sf, open(password_list, 'r') as pl:
        shadow_lines = sf.readlines()
        passwords = pl.readlines()


        for shadow_lines in shadow_lines:
            username, hashed_password = shadow_lines.split(':')[0], shadow_lines.split (':')[1].strip()
            print(f'Checking for user: {username}')
            for password in passwords:
                password = password.strip()
                print(f"Trying password: {password}")
                if sha256_crypt.verify(password, hashed_password):
                    print(f"Password for {username} found: {password}")
                    break

#Call the function
crack_password(shadow_file, password_list)
