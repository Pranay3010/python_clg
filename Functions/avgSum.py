# Wap to calculate avg sum of first n numbers
def TotalSum(n):
    sum =0
    for i in range(1,n+1):
        sum=sum+i
    
    print(f"Sum is {sum}")

    avg = sum/n
    print(f"Avg sum is {avg}")

x=int(input("Enter the Value of n: "))
TotalSum(x)