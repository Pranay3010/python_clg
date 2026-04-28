import random as r

guess=(input("Enter the Char :"))

target=r.choice("Pranay")

while True:
    if(target==guess):
        print("You guess it right")
        break
    else:
        print("Try again")
        guess=(input("Enter the Char :"))

