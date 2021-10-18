from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from model import models

    # 블루프린트
    from views import post_views, auth_views
    app.register_blueprint(post_views.bp)
    app.register_blueprint(auth_views.bp)

    #jwt
    jwt = JWTManager(app)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
