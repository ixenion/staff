#function definition:
def greet():
    print('Hi there', end='\n')
    print('welcome aboard captain')

#functuon call:
greet()

#######################################

def grt(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')
grt("John", "Smith")
grt(first_name="J", last_name="S")#key word arguments. makes code more readable
grt("J", last_name="S")#combination
#grt(first_name="J", "S") ERROR Key word arguments only after positional arguments


######################################
##function return value##

def square(number):
    return number * number
print(square(3))

####################################
##emoji_function##

def emoji_onverter(message):
    words = message.split(" ")
    emojis = {
            ":)": "😄",
            ":(": "😧"
            }
    output = ""
    for wor in words:
        output += emojis.get(word, word) + " "
    return output

message = input('emoji: ')
print(emoji_converter(message))

###################################


