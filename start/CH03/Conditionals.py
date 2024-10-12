#!/usr/bin/env python3
# example workign with conditionals
#By 
import time


# Function to get valid input from user
def get_pirate_input():
    while True:
        response = input("ARRRR! Ye ready to fire the cannons? (y/n): ")
        if response in ['y', 'n']:
            return response
        else: print("Avast! That is not a proper saying! Enter y or n")

# Function to reload cannons

def reload_cannons():
    print("Arrrr! Ye be reloading our cannons hold fast for 5 seconds")
    time.sleep(5)
    print("The cannons are ready to fire")

# Function to fire 5 cannonballs
def fire_cannons():
    for cannon in range (1,6):
        print(f"Cannons away")

# Get input and check our response

response = get_pirate_input()

if response == 'y':
    # Fire first round of cannons
    fire_cannons()
    # Reload the cannons
    reload_cannons()
    # Fire one last time
    fire_cannons()
else:
    print("Arrr Ye this is wrong")
