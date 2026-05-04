def add(a,b):     #parameters
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divison(a,b):
    return a/b
def Modulus(a,b):
    return a%b

a=int(input("Enter the value of A: "))
b=int(input("Enter the value of B: "))

while True:
    
    operation=int(input("Enter the Operation For Addition:1 , Substraction:2, Multiplication:3 , Division:4 , Modulus:5  , Exit:6 ->"))

    if(operation==1):
        print("Addition Of A and B is :",add(a,b))
    elif(operation==2):
        print("Subtraction Of A and B is :",sub(a,b))
    elif(operation==3):
        print("Multiplication Of A and B is :",mul(a,b))
    elif(operation==4):
        print("Divison Of A and B is :",divison(a,b))
    elif(operation==5):
        print("Modulus Of A and B is :",Modulus(a,b))
    elif(operation==6):
        break
    else:
        print("Enter Valid Input")
