'''
    딕셔너리
    1. {key:value, key1:value1, ...} 표현
    2. 순서가 없다
    3. dict(표현식) 함수
       dict(key=value,key2=value2,...)
       dict([ 'ab', ])  a=key b=value
       dict([[k,v],[k1,v1])  k,k1=key v1,v2=value
'''
print(dir(dict))
'''
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
'pop', 'popitem', 'setdefault', 'update', 'values'
'''
# 1. dict 생성
m = {"name":"홍길동", "age":20}
m2 = dict(name="이순신", age=20) # (***)
m3 = dict([['name',"유관순"],["age",20]])
m4 = {} #empty dict
print(m)
print(m2)
print(m3)
print(m4)
