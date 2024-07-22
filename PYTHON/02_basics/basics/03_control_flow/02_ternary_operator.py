# Usual if state:
age = input('Enter your age:')

if int(age) >= 18:
    ticket_price = 20
else:
    ticket_price = 5

print(f"The ticket price is {ticket_price}")


# Ternary operator:
ticket_price = 20 if int(age) >= 18 else 5
print(f"The ticket price is {ticket_price}")
