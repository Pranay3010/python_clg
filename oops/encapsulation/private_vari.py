class Student:
    def __init__(self, name, age, location, hobbies):
        self.__name = name   # private variable
        self.age = age
        self.location = location
        self.hobbies = hobbies

    def study(self):
        return "Student is Studying"

    # Getter
    @property
    def hello(self):
        return self.__name

    # Setter
    @hello.setter
    def hello(self, name):
        self.__name = name


# Object
User1 = Student("Pranay", 20, "Indore", "Cricket")

# Access name
print(User1.hello)

# Modify name
User1.hello = "Rahul"
print(User1.hello)

User1.hello="Alok"
print(User1.hello)




# If you want simple method (no property):
# def getName(self):
#     return self.__name

# Then call:

# print(User1.getName())