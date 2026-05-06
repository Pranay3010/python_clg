class Vehicle:
    def move(self):
        return "Moving"

class Car(Vehicle):
    def Number_of_wheels(self):
        return 4


Scross = Car()

print(Scross.Number_of_wheels())
print(Scross.move())