from datetime import datetime
from flask import Blueprint, render_template, url_for, request
from flask_paginate import Pagination, get_page_parameter

from werkzeug.utils import redirect
from app import db
from form import PostForm
from service import post_service

bp = Blueprint('post', __name__, url_prefix='/')


@bp.route('/', methods=["GET"])
def post_list():
    return post_service.get_post_list()


@bp.route('/detail/<int:post_id>/')
def detail(post_id):
    return post_service.get_detail(post_id)


@bp.route('/create', methods=['POST'])
def create():
    return post_service.create_post()


@bp.route('/delete/<int:post_id>', methods=['DELETE'])
def delete(post_id):
    return post_service.delete_post(post_id)


@bp.route('/modify/<int:post_id>', methods=['PATCH', 'PUT'])
def modify(post_id):
     return post_service.modify_post(post_id)
