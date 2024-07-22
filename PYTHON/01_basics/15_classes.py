#used to define new types
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.draw()

point1.x = 10#set atribute "x" to already existed "move" and "draw"
point1.y = 20
print(point1.x)

class Line:
    def __init__(self, x, y):############################################
        self.x = x###############init objects (onstruct function)########
        self.y = y#######################################################

    def move(self):
        print("move")

    def draw(draw):
        print("draw")

point = Line(10, 20)
print(point.x)#return 10
point.x = 11
print(point.x)#ret. 11

############################################################

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("Name")
john.talk()

john = Person("John Smith")
print(john.name)

bob = Person("Bob Dilan")
bob.talk()

###########################################################

class Katana:
    curve = "curved"

    @staticmethod
    def ex_static_method():
        print("statick method")

    @classmethod
    def ex_class_method(cls):
        print("class method")

    #usual_method
    def ex_method(self):
        print("method")

#static and class methods may be called without object, except ex_method
Katana.ex_static_method()
Katana.ex_class_method()
#print(ex_method) returns error
k = Katana()
k.ex_method()

##########################################################
##class constructor and sample class initialization

#class constructor is __new__(cls, *args, **kwargs) method
#for class initialization used __init__(self) method

class R:
    def __new__(cls, *args, **kwargs):
        print("Hello from __new__")



class Person:
    def __init__(self, width):
        self.width = width

    def talk(self):
        print(f"Hi, I am {self.width}")

john = Person("Name")
john.talk()

john = Person("John Smith")
print(john.width)

bob = Person("Bob Dilan")
bob.talk()

