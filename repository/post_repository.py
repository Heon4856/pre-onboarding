from model.models import Post
from app import db


def post_list(page):
    post_list = Post.query.order_by(Post.create_date.desc()).paginate(page , per_page=10)
    return post_list.items


def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return post


def create(subject, content, date, current_user):
    post = Post(subject=subject, content=content, create_date=date, user_id=current_user)
    db.session.add(post)
    db.session.commit()


def delete(post_id, current_user_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id == current_user_id:
        db.session.delete(post)
        db.session.commit()
        return True
    return False


def modify(post_id, subject, content, modify_date, current_user_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id == current_user_id:
        post.content = content
        post.subject = subject
        post.modify_date = modify_date
        db.session.commit()
        return True
    return False
