def factorial(n):
    fact =1
    for i in range(n,1,-1):
        fact=fact*i

    return fact
x=int(input("Enter the Number:"))
print(factorial(x))