from flask import Blueprint, make_response
from flask_apispec import marshal_with, use_kwargs
from service import post_service
from serializers.post import PostListSchema, PostSchema, CreatePostRequestSchema

bp = Blueprint('post', __name__, url_prefix='/')


@bp.route('/', methods=["GET"])
@marshal_with(PostListSchema(many=True))
def post_list():
    return post_service.get_post_list()


@bp.route('/detail/<int:post_id>/')
@marshal_with(PostSchema)
def detail(post_id):
    return post_service.get_detail(post_id)


@bp.route('/create', methods=['POST'])
@use_kwargs(CreatePostRequestSchema)
@marshal_with(None, code=201)
def create(subject, content):
    post_service.create_post(subject, content)
    return make_response('success',201)


@bp.route('/delete/<int:post_id>', methods=['DELETE'])
def delete(post_id):
    return post_service.delete_post(post_id)


@bp.route('/modify/<int:post_id>', methods=['PATCH', 'PUT'])
def modify(post_id):
    return post_service.modify_post(post_id)
