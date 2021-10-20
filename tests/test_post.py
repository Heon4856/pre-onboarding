import unittest
from app import config, db
import json
from app import create_app
from model.models import User,Post
from datetime import datetime

class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        user1= User(username="test1", password="test1")
        user2 = User(username="test2", password="test2")
        post1 = Post(subject="subject", content="content", create_date=datetime.now(), user_id=1)
        db.session.add(post1)
        db.session.add(user1)
        db.session.add(user2)

        db.session.commit()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_post(self):
        test_data = {"username": "test1", "password": "test1"}
        rv2 = self.client.post('/auth/login/', data=json.dumps(test_data), content_type='application/json')
        json_data = rv2.get_json()
        access_token = json_data["access_token"]
        test_data2 = {"subject": "test3", "content": "test"}
        rv = self.client.post('/create', data=json.dumps(test_data2), content_type='application/json',
                         headers={"Authorization": "Bearer {}".format(access_token)})

        assert 201 == rv.status_code

    def test_base_route2(self):
        url = '/'
        response = self.client.get(url)
        print(response.get_json())
        assert 200 == response.status_code

    def test_base_route(self):
        url = '/detail/1/'
        response = self.client.get(url)
        assert 200 == response.status_code

    def test_modify(self):
        test_data = {"username": "test1", "password": "test1"}
        rv = self.client.post('/auth/login/', data=json.dumps(test_data), content_type='application/json')
        json_data = rv.get_json()
        access_token = json_data["access_token"]
        test_data2 = {"subject": "modify", "content": "test"}
        rv = self.client.patch('/modify/1', data=json.dumps(test_data2), content_type='application/json',
                          headers={"Authorization": "Bearer {}".format(access_token)})
        assert 200 == rv.status_code

    def test_delete(self):
        test_data = {"username": "test1", "password": "test1"}
        rv = self.client.post('/auth/login/', data=json.dumps(test_data), content_type='application/json')
        json_data = rv.get_json()
        access_token = json_data["access_token"]
        rv = self.client.delete('/delete/1', headers={"Authorization": "Bearer {}".format(access_token)})
        assert 204 == rv.status_code


if __name__ == '__main__':
    unittest.main()
