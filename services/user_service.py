import email
from threading import local
from models.user_model import User
from .engine import Session, engine
from sqlalchemy import exists

local_session = Session(bind = engine)


def create_user(name_p, password_p, email_p, role_p):
        local_session.add(User(name_p, password_p, email_p, role_p))
        local_session.commit()

def read_all():
        users = local_session.query(User).all()
        return users

def read_byID(id):
        user = local_session.query(User).filter(User.id == id).first()
        return user

def read_byUsername(username):
        user = local_session.query(User).filter(User.username == username).first()
        return user

def update_user(user):
        user_to_update = read_byID(user.id)
        user_to_update.username = user.username
        user_to_update.email = user.email
        local_session.commit()

def delete_user(user):
        local_session.delete(user)
        local_session.commit()

def checkUsernameExist(username):
        ret = local_session.query(exists().where(User.username == username)).scalar()
        return ret 

def checkEmailExist(email):
        ret = local_session.query(exists().where(User.email == email)).scalar()
        return ret

def getAllOperators():
        ops = local_session.query(User).filter(User.role == 1).all()
        return ops



# if __name__ == "__main__":
#     User_Service.create_user("New UserTest", "newusertest3@mail.com")

# users = User_Service.read_all()

# for u in users:
#     print(u.id, u.username)

# user = User_Service.read_byID(3)
# print(user)

# user = User_Service.read_byID(1)
# user.username = "NewUserUpdatedv2"
# user.email = "newuserupdatedv2@mail.com"

# User_Service.update_user(user)

# User_Service.delete_user(user)