
x = int(input("Enter the Number: "))

try:

    print(10/x)

except(ZeroDivisionError):
    print("10 is not divisble by zero")
except(ValueError):
    print("Can't enter string or char")  


# Catch-all for unexpected errors. Log this in production!
except Exception as e:
    print("Unexpected Error:", e)

else:
    print("try block runs:")

finally:
    print("last block of code is running")

    
