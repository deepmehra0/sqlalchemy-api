
from models.user import User_Model


def authenticate(username, password):
    print(username)
    print(password)
    user = User_Model.user_details(username)
    print(user.password)
    print(user.username)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return User_Model.find_by_id(user_id)