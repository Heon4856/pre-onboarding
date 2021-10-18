# 1. 구현한 방법과 이유
1. 확장가능성 및 의존성을 낮추기 위해서 레이어를 나누었습니다.
2. 과제가 무거운 것이 아니라, 게시판 CRUD API이기 때문에, Flask로 개발하였습니다.
3. 오류가 나는 경우에는 어떠한 오류가 예상되는 지 알려주고자 하였습니다.
4. 인증 인가로는 jwt토큰 방식을 사용하였습니다. 이는 세션을 통한 방식과 달리 서버측 부하를 낮출 수 있기 때문입니다.



# 2. 실행 방법
```shell
pip install -r requirements.txt
```
```shell
flask db init
```
```shell
flask db migrate
```


# 3. api명세