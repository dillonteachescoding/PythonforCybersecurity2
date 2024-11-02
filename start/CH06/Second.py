from passlib.hash import sha512_crypt

# File paths
ShadowFile = r"/home/justincase/Desktop/IT 102/PythonforCybersecurity2/start/CH06/shadow"

PasswordFile = r"/home/justincase/Desktop/IT 102/PythonforCybersecurity2/start/CH06/top1000.txt"


# Function to guess passwords
def GuessPassword(ShadowFile, PasswordFile):
    with open(ShadowFile, 'r') as sf, open(PasswordFile, 'r') as pf:
        shadows = sf.readlines()
        passwords = pf.readlines()

        for shadow in shadows:
            # Split once and unpack the results, skipping lines without a valid hash
            parts = shadow.split(':')
            if len(parts) < 2 or '!' in parts[1] or '*' in parts[1]:
                continue  # Skip this line if no hash is found

            Username, HashPassword = parts[0], parts[1].strip()
            
            print(f'Checking for user: {Username}')
            for password in passwords:
                password = password.strip()
                print(f'Trying password: {password}')
                
                # Attempt to verify if the password matches the SHA-512 hash
                try:
                    if sha512_crypt.verify(password, HashPassword):
                        print(f'Password for {Username} found! It is {password}')
                        break
                except ValueError:
                    print(f"Skipping invalid hash for {Username}")

# Call the function
GuessPassword(ShadowFile, PasswordFile)
