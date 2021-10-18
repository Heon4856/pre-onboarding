from model.models import User
from app import db


def signup(username,password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

def login(username,password):
    user = User.query.filter_by(username=username).first()
    if user.password == password:
        return user.id
    else:
        return 0


