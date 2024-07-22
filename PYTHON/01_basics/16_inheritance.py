#mechanism for reusing code. (for copy classes)

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")
    pass#                ##python dont like empty classes

class Cat(Mammal):
    pass

cat1 = Cat()
cat1.walk()

dog1 = Dog()
dog1.walk()
dog1.bark()

