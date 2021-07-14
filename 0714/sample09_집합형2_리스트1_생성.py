'''
    리스트 생성밥법
    1. []표현
    2. [값,값2,...]
        [] empty리스트
    3. list() 함수
    ==> 값은 문자열 또는 tuple
    4. 저장되는 값은 데이터형이 달라도 가능하다.
'''

#1. 리스트 생성
string_list = ["홍길동","이순신"]
int_list = [10,20,30]
empty_list = []
mixed_list = [10,"홍길동",True]
nested_list = [['A','B','C'],[10,20,30]]
print(string_list)
print(int_list)
print(empty_list)
print(mixed_list)
print(nested_list)

str_list = list("Hello")
print(str_list) # ['H', 'e', 'l', 'l', 'o']
tuple_list = list((10,20,30))
print(tuple_list) # [10, 20, 30]