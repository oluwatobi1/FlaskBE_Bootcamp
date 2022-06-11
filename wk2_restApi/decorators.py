# decorators modify the behavior of a function
# decorators are functions that modify the behavior of a function

from readline import get_begidx
from keyring import get_password


user = {"username": "freeman", "password": "1234", "email": "", "access": "guest"}



def make_secure(func):
    def secure_password(*args, **kwargs):
        if user["access"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"{user['username']} has no access"
    return secure_password

@make_secure
def get_password():
    return user["password"]



print(get_password())

