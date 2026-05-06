class Bank:
    def __init__(self,name,age,account_open_year,balance=0):
        self.name = name
        self.age = age
        self.account_open_year = account_open_year
        self.balance=balance
    
    def display(self):
        return f"Current Balance is : {self.balance}"

    def withdraw(self,withdraw_amount):
        self.withdraw_amount = withdraw_amount

        if (self.withdraw_amount > self.balance and self.withdraw_amount <= 0):
             return f"Amount can't withdraw {self.balance}"
        self.balance=self.balance-self.withdraw_amount
        return f"Current Balance is : {self.balance}"


    def deposite(self,deposite_amount):
        self.deposite_amount=deposite_amount
        self.balance=self.balance + self.deposite_amount

        return f"Current Balance is : {self.balance}"
    
users = {
    "Pranay": Bank("Pranay", 20, 2009, 0),
    "Alok": Bank("Alok", 21, 2009, 0)
}

current_user = None


while current_user is None:
    name = input("Enter your name to login: ")
    if name in users:
        current_user = users[name]
        print(f"Welcome {current_user.name}")
    else:
        print("User not found, try again")


# ✅ Main menu
while True:
    print("\n___________BANK____________")
    print("1. Display Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Switch User")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Enter a valid number")
        continue


    match choice:
        case 1:
            print(current_user.display())

        case 2:
            withdraw_amount=int(input("Enter the amount to withdraw :"))
            print(current_user.withdraw(withdraw_amount))
        
        case 3:
            deposite_amount=int(input("Enter the amount to deposite :"))
            print(current_user.deposite(deposite_amount))


        case 4:
            current_user = None
            while current_user is None:
                name = input("Enter user name to switch: ")
                if name in users:
                    current_user = users[name]
                    print(f"Switched to {current_user.name}")
                else:
                    print("User not found")

        case 5:
            print("Thank you for using the bank system")
            break

        case _:
            print("Invalid choice")
 











# class Bank:
#     def __init__(self,name,age,account_open_year,balance=0):
#         self.name = name
#         self.age = age
#         self.account_open_year = account_open_year
#         self.balance=balance
    
#     def display(self):
#         return f"Current Balance is : {self.balance}"

#     def withdraw(self,withdraw_amount):
#         self.withdraw_amount = withdraw_amount

#         if(self.withdraw_amount>self.balance):
            
#             return f"Amount can't withdraw {self.balance}"
#         self.balance=self.balance-self.withdraw_amount
#         return f"Current Balance is : {self.balance}"


#     def deposite(self,deposite_amount):
#         self.deposite_amount=deposite_amount
#         self.balance=self.balance + self.deposite_amount

#         return f"Current Balance is : {self.balance}"
    
# user1=Bank("Pranay",20,2009,0)
# user2=Bank("Alok",21,2009,0)
# # print(user1.name)

# while True:
#     print("___________BANK____________")
#     print(" 1 For Display Balnce\n 2 For Withdraw\n 3 For Deposite\n")
#     choice =int(input("Enter the choice: "))

#     match choice:
#         case 1:
#             print(user1.display())

#         case 2:
#             withdraw_amount=int(input("Enter the amount to withdraw :"))
#             print(user1.withdraw(withdraw_amount))
        
#         case 3:
#             deposite_amount=int(input("Enter the amount to deposite :"))
#             print(user1.deposite(deposite_amount))

 