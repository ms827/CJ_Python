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
#1. 방법
with con.cursor() as cur:
    sql='''
        insert into employees (employee_id, last_name, email, hire_date, job_id) values
                              (:employee_id, :last_name, :email, sysdate, :job_id)  
                                
'''
    cur.execute(sql, employee_id=997, last_name='홍길동', email='hong2', job_id="IT_PROG")
    print("저장된 레코드개수:",cur.rowcount)
    con.commit()

    cur.execute("select * from employees")
    response = cur.fetchall()
    for row in response:
        print(row)
con.close()


