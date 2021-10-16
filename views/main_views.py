from datetime import datetime
from flask import Blueprint,render_template, url_for, request
from werkzeug.utils import redirect
from model.models import Post
from app import db

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def hello_world():
    return 'Hello World!22'

@bp.route('/posts')
def posts():
    post_list = Post.query.order_by(Post.create_date.desc())
    return render_template('post/post_list.html', post_list=post_list)

@bp.route('/detail/<int:post_id>/')
def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post/post_detail.html', post=post)

@bp.route('/create', methods=('POST','GET'))
def create():
    content = request.form['content']
    post = Post(subject= "title", content=content, create_date=datetime.now())
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('main.posts'))

@bp.route('/delete/<int:post_id>')
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.posts'))



