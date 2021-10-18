from flask import Blueprint, make_response, jsonify,request
from flask_apispec import marshal_with, use_kwargs
from flask_jwt_extended import jwt_required, get_jwt_identity
from service import post_service
from serializers.post import  PostSchema, CreatePostRequestSchema

bp = Blueprint('post', __name__, url_prefix='/')


@bp.route('/', methods=["GET"])
@marshal_with(PostSchema(many=True))
def post_list():
    page = request.args.get('page', type=int, default=1)
    return post_service.get_post_list(page)


@bp.route('/detail/<int:post_id>/')
@marshal_with(PostSchema)
def detail(post_id):
    return post_service.get_detail(post_id)


@bp.route('/create', methods=['POST'])
@jwt_required()
@use_kwargs(CreatePostRequestSchema)
@marshal_with(None, code=201)
def create(subject, content):
    current_user = get_jwt_identity()
    post_service.create_post(subject, content, current_user)
    return jsonify(msg='success', status_code=201)


@bp.route('/delete/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete(post_id):
    current_user = get_jwt_identity()
    if post_service.delete_post_if_user_authorized(post_id, current_user):
        return make_response('', 204)
    return jsonify(msg="권한이 없습니다. 해당 글을 쓰신 유저가 맞는지 확인해주세요.", status_code=401)


@bp.route('/modify/<int:post_id>', methods=['PATCH', 'PUT'])
@jwt_required()
@use_kwargs(CreatePostRequestSchema)
@marshal_with(None, code=200)
def modify(post_id, subject, content):
    current_user = get_jwt_identity()
    if post_service.modify_post_if_user_authorized(post_id, subject, content, current_user):
        return jsonify(msg='success', status_code=200)
    else:
        return jsonify(msg="권한이 없습니다. 해당 글을 쓰신 유저가 맞는지 확인해주세요", status_code=401)
