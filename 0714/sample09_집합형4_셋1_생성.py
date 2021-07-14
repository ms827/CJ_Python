'''
    셋(set)
    1. {값, 값2} 표현
    2. 순서가 없고 중복불가
    3. set() 함수
    4. 저장되는 데이터는 immutable값만 저장 가능.
      예> 상수, 문자열, tuple
        list는 저장 불가
'''
#print(dir(set))
'''
add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
'''
# 1. set 생성
int_set= {10,20,30,20,30,99}
print(int_set)
empty_set = {} # <class 'dict'>
empty_set = set()
print(empty_set, type(empty_set))

str_set = set("hello")
print(str_set)
list_set = set([7,4,2,1,4])
print(list_set)

# 2. mutable 저장 불가
#int_set = {1,2,3,[10,23]} #list는 저장 불가
int_set = {1,2,3,(10,23)} #tuple은 저장 가능
