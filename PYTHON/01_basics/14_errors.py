age = int(input('Age: '))
print(age)

#exit code 0 - success
#exit code 1 - program crashed
# try exept - i used to hande errors

try:
    age = int(input('Age: '))
    income = 10000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:#define what shoul program do if the error is ValueError
    print('Invalid value')#print message instead of crashing

