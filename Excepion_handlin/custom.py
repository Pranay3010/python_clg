class NegativeNumberError(Exception):
    pass

num = int(input("Enter Number: "))

try:
    if num < 0:
        raise NegativeNumberError("Negative number not allowed")

    print("You entered:", num)

except NegativeNumberError as e:
    print("Error:", e)