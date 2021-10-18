from repository import post_repository
from datetime import datetime

def get_post_list():
    return post_repository.post_list()


def get_detail(post_id):
    return post_repository.detail(post_id)

def create_post(subject,content,current_user):
    date = datetime.now()
    return post_repository.create(subject,content,date,current_user)

def delete_post_if_user_authorized(post_id,current_user_id):
    if post_repository.delete(post_id,current_user_id):
        return True
    return False

def modify_post_if_user_authorized(post_id,subject,content,current_user_id):
    modify_date=datetime.now()
    if post_repository.modify(post_id,subject,content,modify_date,current_user_id):
        return True
    return False

