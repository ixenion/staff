from dataclasses import dataclass
import datetime

@dataclass
class User:
    username: str
    created_at: datetime.datetime
    birthday: datetime.datetime | None = None

def validate_user_on_server(_): pass
def check_username(_): pass
def check_birthday(_): pass

def validate_user(user: User):
    """ Checks user, raises exception if something wrong """
    validate_user_on_server(user)
    check_username(user)
    check_birthday(user)

# though "user" must be class
user_id = 123
validate_user(user_id)

