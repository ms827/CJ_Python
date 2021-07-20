import cx_Oracle

con = None
def db_init():
    user = "workshop"
    pw = "workshop"
    dsn = "localhost/xe"
    global con
    con = cx_Oracle.connect(user, pw, dsn, encoding="UTF-8")

def init():

    while(True):
        main_print()
        menu = input("메뉴입력 =>")
        if menu == '1':
            student_all_list()
        elif menu == '2':
            name_search()
        elif menu == '3':
            date_search()
        elif menu == '4':
            number_search()
        elif menu == '5':
            absence_update()
        else:
            exit()

def main_print():
    print("*" * 30)
    print("1. 전체 학생 목록")
    print("2. 학생 이름 검색")
    print("3. 학생 입학년도 범위 검색")
    print("4. 학생 학번으로 다중조회(쉼표구분자)")
    print("5. 학생 휴학 일괄수정")
    print("0. 종료")

# 1. 전체 학생 목록
def student_all_list():
    with con.cursor() as cur:
        print("학번\t\t\t이름\t\t\t\t주민번호\t\t\t\t주소\t\t\t\t\t\t\t입학년도\t\t\t\t휴학여부")
        cnt = 0
        for row in cur.execute("select * from tb_student order by 1 asc"):
            cnt += 1
            ssn = row[3][:8] + "******"
            address = "주소미상             " if row[4] is None else row[4][:11] + "..."
            date = row[5].strftime('%Y/%m/%d')
            print(row[0], "\t", row[2], "\t", ssn, "\t", address, "\t", date, "\t", row[6])

        print("총 학생수:{} 명".format(cnt))

# 2. 학생 이름 조회
def name_search():
    name = input("검색할 학생명을 입력하시오 =>")
    with con.cursor() as cur:
        print("학번\t\t\t이름\t\t\t\t주민번호\t\t\t\t주소\t\t\t\t\t\t\t입학년도\t\t\t\t휴학여부")
        cnt = 0
        for row in cur.execute(f"select * from tb_student where student_name like '%{name}%' order by 1 asc"):
            cnt += 1
            ssn = row[3][:8] + "******"
            address = "***주소미상***             " if row[4] is None else row[4][:11] + "..."
            date = row[5].strftime('%Y/%m/%d')
            print(row[0], "\t", row[2], "\t", ssn, "\t", address, "\t", date, "\t", row[6])
        print("총 학생수:{} 명".format(cnt))

# 3. 학생 입학년도 조회
def date_search():
    start = input("시작 입학년도 입력하시오 =>")
    end = input("끝 입학년도 입력하시오 =>")

    with con.cursor() as cur:
        print("학번\t\t\t이름\t\t\t\t주민번호\t\t\t\t주소\t\t\t\t\t\t\t입학년도\t\t\t\t휴학여부")
        cnt = 0
        for row in cur.execute(f"select * from tb_student where {start} <= to_char(entrance_date,'YYYY') and {end} >= to_char(entrance_date,'YYYY')  order by 1 asc"):
            cnt += 1
            ssn = row[3][:8] + "******"
            address = "***주소미상***             " if row[4] is None else row[4][:11] + "..."
            date = row[5].strftime('%Y/%m/%d')
            print(row[0], "\t", row[2], "\t", ssn, "\t", address, "\t", date, "\t", row[6])
        print("총 학생수:{} 명".format(cnt))

# 4. 학생 학번 다중 조회
def number_search():
    student_no_list = input("검색할 학생의 학번을 입력하시오 =>")
    student_no_list = student_no_list.split(",")
    print(student_no_list)
    with con.cursor() as cur:
        print("학번\t\t\t이름\t\t\t\t주민번호\t\t\t\t주소\t\t\t\t\t\t\t입학년도\t\t\t\t휴학여부")
        cnt = 0
        sql = f"select * from tb_student where student_no IN ( "
        for idx, no in enumerate(student_no_list, 1):
            sql += ("'"+no+"'")
            if idx != len(student_no_list): sql += ","
        sql += ")"
        print(sql)
        for row in cur.execute(sql):
            cnt += 1
            ssn = row[3][:8] + "******"
            address = "***주소미상***             " if row[4] is None else row[4][:11] + "..."
            date = row[5].strftime('%Y/%m/%d')
            print(row[0], "\t", row[2], "\t", ssn, "\t", address, "\t", date, "\t", row[6])
        print("총 학생수:{} 명".format(cnt))

#5.학생 휴학 일괄 수정
def absence_update():
    student_no_list = input("수정할 학생의 학번을 입력하시오 =>")
    student_no_list = student_no_list.split(",")
    print(student_no_list)
    with con.cursor() as cur:
        print("학번\t\t\t이름\t\t\t\t주민번호\t\t\t\t주소\t\t\t\t\t\t\t입학년도\t\t\t\t휴학여부")
        cnt = 0
        sql = f"update tb_student set absence_yn = ( "
        for idx, no in enumerate(student_no_list, 1):
            sql += ("'"+no+"'")
            if idx != len(student_no_list): sql += ","
        sql += ")"
        print(sql)
        cur.execute(sql)
        cnt = cur.rowcount
        print("총 학생수:{} 명".format(cnt))
        con.commit()


if __name__ == '__main__':
    db_init()
    init()