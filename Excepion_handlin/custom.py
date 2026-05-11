# class NegativeNumberError(Exception):
#     pass

# num = int(input("Enter Number: "))

# try:
#     if num < 0:
#         raise NegativeNumberError("Negative number not allowed")

#     print("You entered:", num)

# except NegativeNumberError as e:
#     print("Error:", e)



# class InvalidAgeError(Exception):
#     pass

# age = int(input("Enter age: "))

# try:
#     if age < 18:
#         raise InvalidAgeError("Age must be 18 or above")

#     print("Eligible")

# except InvalidAgeError as e:
#     print(e)


# class InsufficientBalanceError(Exception):
#     pass

# balance = 5000
# withdraw = int(input("Enter amount: "))

# try:
#     if withdraw > balance:
#         raise InsufficientBalanceError("Insufficient balance")

#     balance -= withdraw
#     print("Remaining balance:", balance)

# except InsufficientBalanceError as e:
#     print(e)

class MarksError(Exception):

    def __init__(self, marks):
        self.marks = marks

    def __str__(self):
        return f"Invalid marks: {self.marks}"
        

marks = int(input("Enter marks: "))

try:
    if marks > 100:
        raise MarksError(marks)

    print("Valid Marks")

except MarksError as e:
    print(e)