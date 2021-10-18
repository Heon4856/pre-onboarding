# 1. 구현한 방법과 이유
1. 확장가능성 및 의존성을 낮추기 위해서 레이어를 나누었습니다.
2. 과제가 무거운 것이 아니라, 게시판 CRUD API이기 때문에, Flask로 개발하였습니다.
3. 오류가 나는 경우에는 어떠한 오류가 예상되는 지 알려주고자 하였습니다.
4. 인증 인가로는 jwt토큰 방식을 사용하였습니다. 이는 세션을 통한 방식과 달리 서버측 부하를 낮출 수 있기 때문입니다.
5. 유닛테스트 부분은 완벽하지 않지만, 시도해보았습니다.


# 2. 실행 방법

### 프로젝트 설치

```bash
https://github.com/Heon4856/pre-onboarding.git
```

 ### 환경 구축

```bash
python -m venv venv // 가상 환경 폴더 생성

source venv/[Scripts|bin]/activate // 가상 환경 접속

pip install -r requirements.txt // 필요한 패키지 설치
```

```shell
flask db init
flask db migrate
flask db upgrade
```

```shell
flask run
```


# 3. api명세
https://app.swaggerhub.com/apis-docs/Heon4856/aaxc/1.0.0


### Read -post_list
```shell
curl -X GET "http://localhost:5000/" -H "accept: application/json"

[
  {
    "content": "지울 것",
    "create_date": "2021-10-18T15:05:53.119194",
    "id": 43,
    "modify_date": null,
    "subject": "지워보자"
  },
  {
    "content": "지울 것",
    "create_date": "2021-10-18T15:05:52.952255",
    "id": 42,
    "modify_date": null,
    "subject": "지워보자"
  },
  {
    "content": "지울 것",
    "create_date": "2021-10-18T15:05:52.649007",
    "id": 41,
    "modify_date": null,
    "subject": "지워보자"
  },
  {
    "content": "지울 것",
    "create_date": "2021-10-18T15:05:52.462845",
    "id": 40,
    "modify_date": null,
    "subject": "지워보자"
  },
  {
    "content": "지울 것",
    "create_date": "2021-10-18T15:05:52.272159",
    "id": 39,
    "modify_date": null,
    "subject": "지워보자"
  },
  {
    "content": "지울 것",
    "create_date": "2021-10-18T15:05:52.095329",
    "id": 38,
    "modify_date": null,
    "subject": "지워보자"
  },
  {
    "content": "지울 것",
    "create_date": "2021-10-18T15:05:51.910227",
    "id": 37,
    "modify_date": null,
    "subject": "지워보자"
  },
  {
    "content": "지울 것",
    "create_date": "2021-10-18T15:05:51.734569",
    "id": 36,
    "modify_date": null,
    "subject": "지워보자"
  },
  {
    "content": "지울 것",
    "create_date": "2021-10-18T15:05:51.566497",
    "id": 35,
    "modify_date": null,
    "subject": "지워보자"
  },
  {
    "content": "지울 것",
    "create_date": "2021-10-18T15:05:51.385798",
    "id": 34,
    "modify_date": null,
    "subject": "지워보자"
  }
]
```

### Read -post

```shell
curl -X GET "http://localhost:5000/detail/1/" -H "accept: application/json"
```

```shell
{
  "content": "게시글",
  "create_date": "2021-10-18T14:26:54.177247",
  "id": 1,
  "modify_date": null,
  "subject": "게시글"
}
```

### Create
```shell
curl -X POST "http://localhost:5000/create" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"content\": \"string\", \"subject\": \"string\"}"
```
```shell
{
    "msg": "success",
    "status_code": 201
}
```

### Delete
```shell
curl -X DELETE "http://127.0.0.1:5000/delete/1" -H "accept: application/json"```
```
```shell
(204 NO CONTENT 만 옵니다.)
```

### Modify
```shell
curl -X PATCH "http://localhost:5000/modify/11" -H "accept: application/json"  -H "Content-Type: application/json" -d "{ \"content\": \"string\", \"subject\": \"string\"}"
```
```shell
{
    "msg": "success",
    "status_code": 200
}
```

### 로그인
```shell
curl -X POST "http://localhost:5000/auth/login/" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"password\": \"string\", \"username\": \"string\"}"
```

```shell
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNDU0MzY4MSwianRpIjoiMTE3NzcyMmUtNmQ0MS00M2Y2LTg5YTktZGI0YTBlYTZlZmEwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6NCwibmJmIjoxNjM0NTQzNjgxLCJleHAiOjE2MzQ1NDQ1ODF9.-22JE3F9LySXfKdKByS-8-VB6N3NDdU2p_ZtCqC1m8Y",
  "status_code": 200
}
```

### 회원가입
```shell
curl -X POST "http://localhost:5000/auth/signup/" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"password\": \"stri1231ng11\", \"username\": \"strinsdfg\"}"
```
```shell
{
  "msg": "strinsdfg signup success",
  "status_code": 201
}
```

