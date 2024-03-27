#generate random numbers
import random# random is buil in module, located /usr/lib/python3.7/

x = random.random()#generates random value between 0 and 1
print(x)

for i in range(3):
    print(random.random())

print(random.randint(10, 20))# random values between 10 and 20

#random from list:

members = ['John', 'Bob', 'Tim','Mosh']
print(random.choice(members))

###########################################################
##dice_first

first = [1, 2, 3, 4, 5, 6]

x = random.choice(first)
y = random.choice(first)
print(f"({x}, {y})")#like two dices

##dice_second
print("")

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

dice = Dice()
print(dice.roll())

