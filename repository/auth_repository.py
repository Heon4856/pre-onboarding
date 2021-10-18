from model.models import User
from app import db


def signup(username,password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
#
# def delete(post_id):
#     post = Post.query.get_or_404(post_id)
#     db.session.delete(post)
#     db.session.commit()
#
#
# def modify(post_id,subject,content,modify_date):
#     post = Post.query.get_or_404(post_id)
#     post.content=content
#     post.subject=subject
#     post.modify_date=modify_date
#     db.session.commit()
