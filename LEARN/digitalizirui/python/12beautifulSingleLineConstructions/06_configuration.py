class User:
    def __init__(self, group: str):
        self.group = group

user = User(group="admin")

if user.group == "admin":
    process_admin_request(user, request)
elif user.group == "manager":
    process_manager_request(user, request)
elif user.group == "client":
    process_client_request(user, request)


# simplier
group_to_process = {
        "admin": process_admin_request,
        "manager": process_manager_request,
        "client": process_client_request
        }

group_to_process[user.group](user, request)

