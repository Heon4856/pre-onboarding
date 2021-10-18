from repository import auth_repository
from flask_jwt_extended import create_access_token


def signup(username, password):
    return auth_repository.signup(username, password)


def login(username, password):
    user_id_num = auth_repository.login(username, password)
    if user_id_num > 0:
        return create_access_token(user_id_num)
