from model.models import Post


def post_list():
    post_list = Post.query.order_by(Post.create_date.desc())
    return post_list

def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return post

def create():
    post = Post(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
    db.session.add(post)
    db.session.commit()
    return 200

def delete():
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return 200


def modify():
    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        form = PostForm()
        if form.validate_on_submit():
            form.populate_obj(post)
            post.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
        return redirect(url_for('main.detail', post_id=post_id))