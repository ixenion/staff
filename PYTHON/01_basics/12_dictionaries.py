#to store information that comes as key value pairs
#Name: John Smith "Name is the key which is associated whith value "John Smith"
#Email: john@gmail.com
#whith dictionary we an store a bunch of key value pairs.
#to define:
customer = {
        "name": "John Smith",
        "age": 30,
        "is_verified": True
}
#keys should be unique
#to access:
print(customer["name"])

#print(customer.get(["berthday"])) #returns None value
#print(customer.get["berthday", "1984"])#instead of getting None we get this default value (1984)
customer["name"] = "Jack Smith"# to uppdate information in the key value
customer["berthday"] = "1984"#to add new pair

###########################################
##exercise##
##########################################
##convert digits in words##
##########################################

nums = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero"
        }

number = input('number> ')
for i in number:
    print(nums[i], end=' ')

##another_way##

output = ""
for i in number:
    output += nums.get(i, "err") + " "
print(output)

##emoji##

message = input("smile> ")
words = message.split(' ')#split message by space
emojis = {
        ":)": "😄",
        ":(": "😧"
        }
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

