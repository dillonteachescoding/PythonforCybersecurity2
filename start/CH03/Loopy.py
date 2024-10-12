#!/usr/bin/env python3
# example workign with Loops
#By 

def get_input():
    while True:
        response = input("Is today a great day? (y/n): ".lower())
        if response in ['y', 'n']:
            return response
        else:
            print("invalid response please print y or n")

# Get input and check response
response = get_input()

if response == 'y':
    for _ in range(10):
        print("yes it is")
else:
    print("today is not the best day")