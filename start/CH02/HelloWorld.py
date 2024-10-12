#We want to create a script that takes user input
#and outputs hello there name, as well as have a good
#day

name = input("Hello there, what is your name? ")

print(f"Hello, {name}")

print(f"Today is going to be a great day. {name}")

# Prompt user for there age
age = int(input("How old are you: "))

future_age = age + 2


print(f"You are {future_age} in two years")