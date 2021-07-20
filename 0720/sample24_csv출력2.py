'''
    1.csv 모듈
        import csv
'''

import csv

list_value =[[10,20,30],[44,55,66],[70,80,90]]
try:
    with open("./resource/minseok.csv", "w", encoding="utf-8", newline="") as f:
       writer = csv.writer(f)
       writer.writerow(["국어","수학","영어"]) # 필요시 header 저장
       writer.writerows(list_value)
       # for data in list_value:
       #     writer.writerow(data)
except Exception as e:
    print("Error:",e)

print("end")