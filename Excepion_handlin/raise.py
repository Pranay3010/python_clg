def process_refund(amount):
    if amount < 0:
        raise ValueError("Refund amount cannot be negative.")
    
    return f"Refund of ₹{amount} processed successfully."

try:
    x = int(input("Enter the refund Amount: "))
    print(process_refund(x))

except ValueError as e:
    print(e)