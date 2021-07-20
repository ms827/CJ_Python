'''
    JSON (JavaScript Object Notation: 자바스크립트 객체 표현식)

    1. 배열 객체 표현식
      - 파이썬의 리스트와 비슷
      - [값,값2,...]
      -
    2. 객체 표현식
      - 파이썬의 dict와 비슷
      - {"key":value, ...} key는 "" 만 사용

    --> 매우 중요하다
        현업에서 사용되는 공통적(언어독립,OS독립...)으로 사용되는 데이터 포멧이기 때문이다

'''
import json
# 1. 문자열 ==> JSON 객체로 변환
# "[10,20,30]" ==> [10,20,30]
str_format = "[10,20,30]"
print(str_format, type(str_format))

json_format = json.loads(str_format)
print(json_format, type(json_format))
print(json_format[0])

str_format = '{"username": "홍길동", "age":20}'  # 겉은 '' 사용
json_format = json.loads(str_format)
print(json_format["username"], json_format["age"]) #key값이 없으면 에러
print(json_format.get("username"), json_format.get("age")) #key값이 없으면 Do nothing



# 2. JSON객체 ==> 문자열
# [10,20,30] ==> "[10,20,30]"

json_format = [10,20,30,"홍길동"]
json_format = {"username":"홍길동","age":20}
str_format = json.dumps(json_format, ensure_ascii=False) # ensure_ascii=False 문자처리
print(str_format,type(str_format))