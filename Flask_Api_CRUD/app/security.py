from werkzeug.security import safe_str_cmp #this is for leagacy support
from models.user import UserModel 
from flask_jwt import JWT, jwt_required
#user authentication
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,  password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

