from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec import FlaskApiSpec

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)
    if test_config ==None:
        app.config.from_object(config)
    else:
        app.config.from_object(config.Testing)

    apispec = APISpec(
        title='preonboard',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()],
    )
    app.config.update({
        'APISPEC_SPEC': apispec
    })
    docs = FlaskApiSpec(app=app, document_options=False)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from model import models

    # 블루프린트
    from views import post_views, auth_views
    app.register_blueprint(post_views.bp)
    app.register_blueprint(auth_views.bp)

    # jwt
    jwt = JWTManager(app)

    docs.register(post_views.post_list, blueprint=post_views.bp.name)
    docs.register(post_views.create, blueprint=post_views.bp.name)
    docs.register(post_views.modify, blueprint=post_views.bp.name)
    docs.register(post_views.detail, blueprint=post_views.bp.name)
    docs.register(post_views.delete, blueprint=post_views.bp.name)

    docs.register(auth_views.signup, blueprint=auth_views.bp.name)
    docs.register(auth_views.login, blueprint=auth_views.bp.name)

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify(msg="없는 페이지 입니다. 아마 존재하지 않는 게시글 id로 요청을 보내셨을 가능성이 높습니다.", status_code=404)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
