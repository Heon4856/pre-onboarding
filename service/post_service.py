from repository import post_repository

def get_post_list():
    return post_repository.post_list()


def get_detail(post_id):
    return post_repository.detail(post_id)

def create_post():
    return post_repository.create()

def delete_post(post_id):
    return post_repository.delete(post_id)

def modify_post(post_id):
    return post_repository.modify(post_id)