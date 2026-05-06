class Student:
    def __init__(self,name,age,location,hobbies):
        self.name=name
        self.age=age
        self.location=location
        self.hobbies=hobbies

    def study(self):
        return("Student is Studying")
    

S1=Student("Pranay",20,"Indore","Swiming")
S2=Student("Alok",21,"Indore","Reading")
S3=Student("Vicky",20,"Indore","Singing")
S4=Student("Disha",21,"Indore","Dancing")
S5=Student("Jay",20,"Indore","Swiming")
print(S1.name)
print(S1.age)
print(S1.study())