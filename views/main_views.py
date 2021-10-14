from flask import Blueprint,render_template
from model.models import Post

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def hello_world():
    return 'Hello World!22'

@bp.route('/posts')
def posts():
    post_list = Post.query.order_by(Post.create_date.desc())
    return render_template('post/post_list.html', post_list=post_list)

@bp.route('/posts/<int:post_id>/')
def detail(post_id):
    post = Post.query.get(post_id)
    return render_template('post/post_detail.html', post=post)