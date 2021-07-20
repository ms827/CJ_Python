'''
    날짜와 시간 처리

    1. import time

    2. from datetime import datetime

'''

import time

print("1. 현재시간 구하기:", time.time()) #모든 프로그램언어의 기준시간(1970/1/1) ~ 현재시간까지의 초(second) 반환

print("2. 익숙한 날짜와 시간 구하기")
time_date = time.localtime(time.time())
print(time_date) # time.struct_time(tm_year=2021, tm_mon=7, tm_mday=20, tm_hour=11, tm_min=15, tm_sec=52, tm_wday=1, tm_yday=201, tm_isdst=0)

print("1) 년도:",time_date.tm_year)
print("2) 월:",time_date.tm_mon)
print("3) 일:",time_date.tm_mday)
print("4) 시:",time_date.tm_hour)
print("5) 분:",time_date.tm_min)
print("6) 초:",time_date.tm_sec)

print("3. 날짜 --> 문자열의 포맷") # to_char(sysdate, 'YYYY/mm/dd')
time_date = time.localtime(time.time())
print(type(time_date)) # <class 'time.struct_time'>

str_time_date = time.strftime("%Y-%m-%d, %H:%M:%S (%A) %p",time_date)
print(str_time_date)

print("4.동작을 delay 하기")
print("start")
time.sleep(30)
print("end")