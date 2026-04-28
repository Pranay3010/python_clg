user_name ="Pranay"
password="1234" 

user_name_input=input("Enter your username: ")
password_input=input("Enter your password: ")

if (user_name_input==user_name and password_input==password):
    print("Login successful")
else:
    print("Invalid username or password")
