print("------------------ATM--------------")

def withdraw(c_balance,amount):
    if amount > c_balance :
        print("Invalid Amount Can`t withdraw : Insuffician Balance")
    else:
        c_balance=c_balance-amount
        print(f"Successfully Withdraw {amount}")
    return c_balance
    
def deposite(c_balance,d_amount):
    c_balance=c_balance+d_amount
    print(f"Successfully Deposite {d_amount}")
    return c_balance

def check(c_balance):
    print("Current Balance is :",c_balance)

c_balance = 0


while True:
    Operation=int(input("Select \n 1 for Deposite \n 2 for Withdraw \n 3 for Check \n 4 for Exit \n Enter:"))
    if(Operation==1):
        d_amount = int(input("Enter the amount to Deposite: "))
        c_balance =deposite(c_balance,d_amount)
    elif(Operation==2):
        amount = int(input("Enter the amount to Withdraw: "))
        c_balance = withdraw(c_balance,amount)
    elif(Operation==3):
        check(c_balance)
    elif(Operation==4):
        print("Thankyou for Using ATM")
        break
    else:
        print("Invalid option")
        