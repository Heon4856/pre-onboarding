from model.models import Post
from app import db

def post_list():
    post_list = Post.query.order_by(Post.create_date.desc())
    return post_list

def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return post

def create(subject,content,date):
    post = Post(subject=subject, content=content, create_date=date)
    db.session.add(post)
    db.session.commit()

def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()


def modify(post_id,subject,content,modify_date):
    post = Post.query.get_or_404(post_id)
    post.content=content
    post.subject=subject
    post.modify_date=modify_date
    db.session.commit()
