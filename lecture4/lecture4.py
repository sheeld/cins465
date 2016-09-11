elements = [1,2,"3",4]
print(elements[-1])

#--------------------------

elements = list(range(5))
print (elements)

#--------------------------

d = {"banana":2} #dictionary

d["bob"] = "alice"

print(d)
print(d.keys())

#--------------------------

pair = (1,2,3,4,5,6,7)
pair = (1,2)

print pair[0]

#--------------------------

x = 5

def set_x(num):
    x = num
    print(x)
    
def global_set_x(num):
    global x
    print(x)
    x=num
    print(x)
    
global_set_x(7)
print(x)

#--------------------------

class Human:
    spec = "H. Sapiens"
    
    def __init__(self, name):  #self in python = this in javascript
        self.name = name
        self.age = 0
        
    def grunt(self):
        return "grunt"
        
    @staticmethod
    def grunt2():
        return "grunt2"
        

class MetaHuman():
    def __init__(self, power, name):
        self.power = power
        Human.__init__(self, name)
        
    def printHuman(self):
        print(str(self.name) + " has " + str(self.power))
        
aHuman = Human("Tracey")
mHuman = MetaHuman(5,"rio")

aHuman.printHuman()
        
aHuman = Human("Tracey")
print(aHuman.name)
print(aHuman.grunt())
print(aHuman.grunt2())
