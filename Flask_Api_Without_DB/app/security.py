from werkzeug.security import safe_str_cmp #this is for leagacy support
from user import User 

#simple JWT sample
users = [
    User(1, 'Mike', '12345')
]
#indexing users
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

#user authentication
def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp (user.password,  password):
        return user
def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

