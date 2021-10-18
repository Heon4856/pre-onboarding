from flask import Blueprint, jsonify
from flask_apispec import use_kwargs, marshal_with,doc
from service import auth_service
from serializers.auth import AuthRequestSchema, TokenSchema

bp = Blueprint('auth', __name__, url_prefix='/auth')

@doc(tags=['auth'], description='회원정보를 저장한다.')
@bp.route('/signup/', methods=['POST'])
@use_kwargs(AuthRequestSchema)
def signup(username, password):
    auth_service.signup(username, password)
    return jsonify(msg='{} signup success'.format(username), status_code=201)

@doc(tags=['auth'], description='회원정보를 받아 accesstoken을 반환한다.')
@bp.route('/login/', methods=['POST'])
@use_kwargs(AuthRequestSchema)
@marshal_with(TokenSchema, code=200)
def login(username, password):
    return jsonify(access_token=auth_service.login(username, password), status_code=200)
