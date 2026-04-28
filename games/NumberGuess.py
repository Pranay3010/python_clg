import random as r
guess= int(input("Enter the Number between 1-10 :"))

target=r.randint(1,10)
count=0

while True:
    count+=1

    if(target==guess):
        print("You guess it Right")
        break

    elif(target<guess):
        print("Guess No. is Big")
        guess= int(input("Enter the Number :"))
        

    elif(target>guess):
        print("Guess No. is Small")
        guess= int(input("Enter the Number :"))

print(f"The user takes {count} chances to guess it right")

