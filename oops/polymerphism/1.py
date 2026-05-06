class Bird:
    def __init__(self):
        pass

    def fly(self):   #polymerphism
        pass

class duck(Bird):

    def fly(self):
        return "Don't fly "
    
class eagle(Bird):

    def fly(self):
        return "Silently fly"
    
class piegon(Bird):

    def fly(self):
        return "Flap Flap"
    
bird1=duck()
print(bird1.fly())

bird2=eagle()
print(bird2.fly())

bird3=piegon()
print(bird3.fly())

