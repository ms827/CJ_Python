'''
    sample2.csv 읽기
    번호|이름|가입일시|나이
1|김정수|2017-01-19 11:30:00|25
2|박민구|2017-02-07 10:22:00|35
3|정순미|2017-01-22 09:10:00|33
4|김정현|2017-02-22 14:09:00|45
5|홍미진|2017-04-01 18:00:00|17
...

    1.csv 모듈
        import csv
'''

import csv

try:
    with open("./resource/sample2.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="|") # delimiter는 구분자 정보 지정

        header = next(f) # header 읽고 제외
        for row_list in reader:
            for row in row_list:
                print(row,end="")
            print()
        # print(list(reader))
except Exception as e:
    print("Error:",e)

print("end")