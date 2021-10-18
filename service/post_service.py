from repository import post_repository
from datetime import datetime

def get_post_list():
    return post_repository.post_list()


def get_detail(post_id):
    return post_repository.detail(post_id)

def create_post(subject,content):
    date = datetime.now()
    return post_repository.create(subject,content,date)

def delete_post(post_id):
    return post_repository.delete(post_id)

def modify_post(post_id):
    return post_repository.modify(post_id)