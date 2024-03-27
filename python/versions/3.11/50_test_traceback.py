data = {
    "users": {
        "admins": {
            "admin@mail.ru": {
                "name": "Alexey"
            },
            "user@mail.ru": None
        }
    }
}

print(data["users"]["admins"]["user@mail.ru"]["name"])
