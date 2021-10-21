import unittest
from app import config, db
import json
from app import create_app
from model.models import User
from werkzeug.security import generate_password_hash


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        user = User(username="test1", password=generate_password_hash("test1"))
        db.session.add(user)
        db.session.commit()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_signup(self):
        """회원가입을 하면 201상태코드를 반환한다."""
        test_data = {"username": "test1100", "password": "test"}
        rv = self.client.post('/auth/signup/', data=json.dumps(test_data), content_type='application/json')
        assert 201 == rv.status_code

    def test_login_api_with_valid_login_information(self):
        """유효한 로그인 정보로 로그인 시도시 200상태코드와 access_token을 반환"""
        test_data = {"username": "test1", "password": "test1"}
        rv = self.client.post('/auth/login/', data=json.dumps(test_data), content_type='application/json')
        print(rv.status_code)
        assert 200 == rv.status_code
        assert b'access_token' in rv.data

    def test_login_with_wrong_password(self):
        """잘못된 비밀번호로 로그인 시도시 404 상태코드를 반환한다."""
        test_data = {"username": "test1", "password": "wrong_password"}
        rv = self.client.post('/auth/login/', data=json.dumps(test_data), content_type='application/json')
        assert 404 == rv.status_code

    def test_login_with_not_found_username(self):
        """찾을 수 없는 유저이름으로 로그인 시도시 404 상태코드를 반환한다."""
        test_data = {"username": "wron_id", "password": "test122"}
        rv = self.client.post('/auth/login/', data=json.dumps(test_data), content_type='application/json')
        assert 404 == rv.status_code


if __name__ == '__main__':
    unittest.main()
