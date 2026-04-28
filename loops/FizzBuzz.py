# (1-100)
# if num/3 print fizz
# if num/5 print Buzz
# if num/15 print fizBuzz

for i in range(1,101):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)