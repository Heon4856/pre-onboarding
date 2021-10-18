from repository import auth_repository


def signup(username,password):
    return auth_repository.signup(username,password)