x=10

print(id(x))  # address of 10:

#  there are stack for storage that stores local variable + reference variable
# heap stores 10;


a=[1,2]
b=[1,2]

print(a==b)
print(a is b)
print(id(a))
print(id(b))

c=20
d=20
print(c is d)
print(id(c))
print(id(d))