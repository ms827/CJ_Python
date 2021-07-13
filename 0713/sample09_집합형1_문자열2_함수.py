'''
    1.문자열 생성
    2.문자열 함수
      --> 문자열.함수()
      --> 문자열의 함수 확인방법
        print(dir(str))
      *Built-ins 의 함수
        -len()함수
        -int(),str(),input(),print,bool(),...
        --> 그냥사용
'''
print(dir(str))
'''
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 
'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

s = "seQUEnce"

print("1. 문자열 길이: ", len(s)) # 8
print("2. 특정문자의 갯수: ", s.count('e')) # 3
print("3. 첫글자 대문자: ", s.capitalize()) # Sequence
print("4. 전체 대문자: ", s.upper()) # SEQUENCE
print("5. 전체 소문자: ", s.lower()) # sequence
print("6. swap 문자: ", s.swapcase()) # SEqueNCE
print("7. 공백제거: ")
x = "     Hello     "
print("lstrip: ", x.lstrip(), len(x.lstrip())) # Hello      10
print("lstrip: ", x.rstrip(), len(x.rstrip())) #      Hello 10
print("strip: ", x.strip(), len(x.strip())) # Hello 5
print("8. 특정문자제거")
x = "HHHHelHoHHHH"
result = x.lstrip('H') #실행결과를 변수에 저장 가능하다
print("lstrip H문자 제거", result) # elHoHHHH
print("rstrip H문자 제거", x.rstrip('H')) # HHHHelHo
print("strip H문자 제거", x.strip('H')) # elHo

print("9. 문자열 변경", "Hello".replace("e","E")) # HEllo

print("10. 구분자로 분리(공백이 기본구분자)")
xx = "홍길동/이순신/유관순"
result = xx.split("/")
print(result) #['홍길동', '이순신', '유관순']
xx = "홍길동1 이순신1 유관순1"
result = xx.split()
print(result) #['홍길동1', '이순신1', '유관순1']


print("11. 특정문자 시작여부: ", "Hello".startswith("H")) #True
print("11. 특정문자 시작여부: ", "Hello".startswith("X")) #False


print("12. 특정문자 종료여부: ", "Hello".endswith("o")) #True
print("12. 특정문자 종료여부: ", "Hello".endswith("x")) #False

print("13. 특정 문자 위치: ", "Hello".find("e")) # 1 (순방향)
print("13. 특정 문자 위치: ", "Hello".find("x")) #-1 (못찾으면 -1)
print("13. 특정 문자 위치: ", "Hello".find("l")) # 2
print("13. 특정 문자 위치: ", "Hello".rfind("l")) # 3 (가장 높은 인덱스, 뒤에서 부터 탐색)

#sql 패딩 역할 --> center, rjust, ljust
print("14. center 패딩: " , "Hello".center(21,"*")) #********Hello********
print("14. rjust 패딩: " , "Hello".rjust(21,"*")) #****************Hello
print("14. ljust 패딩: " , "Hello".ljust(21,"*")) #Hello****************

# 집합형의 값을 특정 문자와 연결 (*)
# ["A","B","C"] == A 와 B 와 C
print("15. 집합형의 값을 특정 문자와 연결 :"," 와 ".join(["A","B","C"])) #A 와 B 와 C

# 문자 / 숫자 여부 확인
print("16. 문자로만 구성?: ", "Hello".isalpha()) #True
print("16. 문자로만 구성?: ", "Hello123".isalpha()) #False
print("17. 숫자로만 구성?: ", "9874".isnumeric()) #True
print("17. 숫자로만 구성?: ", "hello9874".isnumeric()) #False