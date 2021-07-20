import cx_Oracle
import csv
"""
drop table scientist;
create table scientist
(  num  number(4) CONSTRAINT scientist_num_pk PRIMARY KEY,
   name varchar2(20),
   born date,
   died date,
   age number(3),
   occupation varchar2(20));
"""
con = None
def db_init():
    user = "hr"
    pw = "hr"
    dsn = "localhost/xe"
    global con
    con = cx_Oracle.connect(user, pw, dsn, encoding="UTF-8")

    with open("./scientists.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(f)  # header  skip
        scientist_list = []
        for idx, v in enumerate(reader,1):
            v.insert(0, idx)
            scientist_list.append(tuple(v))
        print(scientist_list)
        with con.cursor() as cur:
            sql = f"insert into scientist ( num, name, born, died, age, occupation) " \
                  " values ( :1, :2, :3, :4, :5 , :6 )"
            cur.executemany(sql, scientist_list)
            print("저장된 레코드갯수:", cur.rowcount)
            con.commit()



if __name__ == '__main__':
    db_init()
