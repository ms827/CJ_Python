#멤버쉽 연산자
'''
 1.dict제외한 집합형
 집합형에서 임의의 값 존재여부 확인 ==> 존재하면 True, 없으면 False 반환

 문법:
    값 in 집합형
 2. dict
   dict 에서 임의의 key 존재여부 확인
'''

n = [10,20,30]
n = (10,20,30)
n = {10,20,30}
result = 10 in n
print(result) # True
result = 100 in n # False
print(result)

m = "hello"
print( "h" in m) #True
print( "x" in m) #False

person = {"username":"홍길동","age":20}
print( "username" in person ) #username key 가 존재하냐?
print( "email" in person ) #email key 가 존재하냐?

