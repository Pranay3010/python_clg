from abc import ABC,abstractclassmethod

class Vehicle(ABC):

    def __init__(self):
        pass
    
    @abstractclassmethod        
    def startEngine(self):
        pass

    def move(self):
        return "Moving"

class Car(Vehicle):
    def Number_of_wheels(self):
        return 4
    def startEngine(self):
        return "Vroom Vroom"
    
class Bike(Vehicle):
    def Number_of_wheels(self):
        return 2
    def startEngine(self):
        return "Droom Droom"


Scross=Car()
Ninja=Bike()
# print(Scross.Number_of_wheels())
# print(Scross.startEngine())
# print(Ninja.startEngine())

def start(instance):
    return instance.startEngine() # polymorphism

vs=[Scross,Ninja]

for obj in vs:
    print(start(obj))
