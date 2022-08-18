from models.user import User_Model
def authenticate(username,password):
    user =User_Model.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return User_Model.find_by_userid(user_id)
