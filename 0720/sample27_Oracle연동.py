'''
    오라클 연동
    1. 오라클 연동을 지원하는 모듈 필요, 추가로 설치해야 한다.
      ==> pip install 모듈
      ==> import 모듈(패키지) , Pycharm 도움을 받아서 설치
    pip install cx_Oracle 프로프트에 입력
'''
import cx_Oracle

user = "hr"
pw = "hr"
dsn = "localhost/xe"

con = cx_Oracle.connect(user, pw, dsn, encoding="utf-8")
print(con) #<cx_Oracle.Connection to hr@localhost/xe>


con.close()