# gracefully copy
numbers = [1,2,3]
another_numbers = numbers[:] # copy number list

# reverce list
numbers = [1,2,3]
numbers[::-1]

# conditions
name = "A"
# old method
if name == "B" or name == "C":
    pgerrint(name)
# shorter method
if name in ("B", "C"):
    print(name)

# true conditions
a = b = c = d = e = True
# long method
if a and b and c and d and e:
    pass
# shorter method (if all items are True)
if all( (a,b,c,d,e) ):
    pass
# shorter method (if at least one item is True)
if any( (a,b,c,d,e) ):
    pass

# ternary operator
config = False
# long method
if config == True:
    a = 1
else:
    a = 0
# short method
a = 1 if config else 0

# configuring
class User:
    def __init__(self, group: str):
        self.group = group
user = User(group="admin")
# lond method
if user.group == "admin":
    process_admin_request(user, request)
elif user.group == "manager":
    process_manager_request(user, request)
elif user.group == "client":
    process_client_request(user, request)
# shorter method
group_to_process = {
        "admin":process_admin_request,
        "manager":process_manager_request,
        "client":process_client_request
        }
group_to_process[user.group](user, request)
