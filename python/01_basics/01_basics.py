print('')
print("hello")
print('')
some = 3.14
name = 'john'
# coment
#date = input('when? ')
#fix = 25 + int(date)
#print(fix)
course = 'Python for "gtk"'
print(course)
course = "Python's language"
print(course)
courses= '''
this is
multiline
text
'''
print(courses)

#single symbols:
course = 'rasp'
print(course[0:1])

#two equals:
first = 'John'
sec = 'Karter'
msg1 = first + ' [' + sec + '] is cool'
msg2 = f'{first} [{sec}] is cool' #formatted string
print(len(msg2)) #show length of msg2 variable
print(msg1.upper()) #replace all chars with upper case
print(msg2.lower())
print(msg1.find('K')) #return index of "K"
#print(msg1.replace('cool', 'wery cool')
print('is' in msg1) #true or false
print(10 // 3)    #celoe ot delenya
print(10 % 3)     #ostatok
print(10 ** 3)    #stepen'
round(8.1)          #okrugleniye
abs(-7)            #module

import math       #math module
math.ceil(2.9)    #returns 3
math.floor(2.9)   #ret. 2

#if
ishot = True
iscold = False
if ishot:
 print("it's a hot day")
 print('drink a planty of water')
elif isold:
 print('done warm clothes')
else:
 print('what a heck?')
 
price = 1000
hgc = False
if hgc:
    down = 0.1 * price
else:
    down = 0.2 * price
print(f"Down payment: {down}")

if ishot and not iscold:#    or
    print('all right')

#temp = input('what is the temperature? ')# input() may be (empty)
temp = 2
if int(temp) > 18:
    print('summer')
else:
    print('not summer')

#name = input('your name: ')
name = 'abcd'
ln = len(name)
if ln > 3 and  ln < 15:
    print('good name')
elif ln < 3:
    print('add some chars')
elif ln > 15:
    print('no way!')


#weight = int(input('Weight: '))
#unit = input('(L)bs or (K)g: ')

weight = 168
unit = "l"
if unit.upper() == "L":
    conw = weight * 0.45
    print(f"You are {conw} kilos")
else:
    conw = weight / 0.45
    print(f"You are {conw} pounds")

i = 1
while i <= 5:
    print(i)
    print('*' * i)
    i = 1 + i
print('Done')
print()
print()

secret_number = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Had enough...')



