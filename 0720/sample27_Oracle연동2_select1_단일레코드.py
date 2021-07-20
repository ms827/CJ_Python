'''
    오라클 연동
    1. 오라클 연동을 지원하는 모듈 필요, 추가로 설치해야 한다.
      ==> pip install 모듈
      ==> import 모듈(패키지) , Pycharm 도움을 받아서 설치
    pip install cx_Oracle 프로프트에 입력
'''

'''
cursor 객체의 함수
'arraysize', 'arrayvar', 'bindarraysize', 'bindnames', 'bindvars', 
'callfunc', 'callproc', 'close', 'connection', 'description', 'execute', 
'executemany', 'executemanyprepared', 'fetchall', 'fetchmany', 'fetchone', 
'fetchraw', 'fetchvars', 'getarraydmlrowcounts', 'getbatcherrors', 
'getimplicitresults', 'inputtypehandler', 'lastrowid', 'outputtypehandler', 
'parse', 'prefetchrows', 'prepare', 'rowcount', 'rowfactory', 'scroll', 
'scrollable', 'setinputsizes', 'setoutputsize', 'statement', 'var']

fetch - select 가져올때
'''
import cx_Oracle

user = "hr"
pw = "hr"
dsn = "localhost/xe"

con = cx_Oracle.connect(user, pw, dsn, encoding="utf-8")
print(con) #<cx_Oracle.Connection to hr@localhost/xe>

sql = "select * from employees where employee_id =100" # 프로그램언어 사용시 sql문의 끝의 ; 지정 안함
#1. 방법
with con.cursor() as cur: #with문 cursor 자동으로 close
    cur.execute(sql)
    response = cur.fetchone()
    print(response) #tuple


#2. 방법
with con.cursor() as cur:
    print(dir(cur))
    cur.execute("select * from employees where employee_id =101")
    response = cur.fetchone()
    print(response) #tuple

#3. 방법 : 바인딩 변수 사용
emp_id = input(("emp_id 입력"))
with con.cursor() as cur:
    cur.execute("select * from employees where employee_id = :x", x=emp_id)
    response = cur.fetchone()
    print(response) #tuple
con.close()
