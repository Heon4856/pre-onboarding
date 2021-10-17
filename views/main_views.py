from datetime import datetime
from flask import Blueprint, render_template, url_for, request
from flask_paginate import Pagination, get_page_parameter

from werkzeug.utils import redirect
from model.models import Post
from app import db
from form import PostForm

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def post_list():
    page = request.args.get('page', type=int, default=1)
    post_list = Post.query.order_by(Post.create_date.desc())
    post_list = post_list.paginate(page, per_page=8)
    return render_template('post/post_list.html', post_list=post_list)


@bp.route('/detail/<int:post_id>/')
def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post/post_detail.html', post=post)


@bp.route('/create', methods=('POST', 'GET'))
def create():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        post = Post(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.post_list'))
    return render_template('post/post_form.html', form=form)


@bp.route('/delete/<int:post_id>')
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.post_list'))


@bp.route('/modify/<int:post_id>', methods=('GET', 'POST'))
def modify(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        form = PostForm()
        if form.validate_on_submit():
            form.populate_obj(post)
            post.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
        return redirect(url_for('main.detail', post_id=post_id))
    form = PostForm(obj=post)
    return render_template('post/post_form.html', form=form)
