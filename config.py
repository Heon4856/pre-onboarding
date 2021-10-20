import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'bulletin.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"
JWT_SECRET_KEY = "super-secret"


class Testing:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'testing.sqlite')
    JWT_SECRET_KEY = "super-secret"
