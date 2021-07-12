#집합형 데이터 종류 및 표현 (매우중요 ********)

#2.리스트(list) :순서가 있고 중복허용, 값 변경 가능 (mutable)
print("리스트: >> ", [10,20,30,20,30])
print("리스트: >> ", ["A","B","C"])
print("리스트: >> ", ["A","B","C",10,20,41.4,True]) #서로 다른 데이터 저장 가능
print("리스트: >> ", []) #empty list

num = [10,20,30,20,30]
print(num[0]) #리스트의 요소 접근방법은 [위치값], 위치값을 첨자(인덱스)라고 부른다.
num[0]=100
print(num)

# 3. 튜플(tuple) : 순서가 있고 중복허요, 값 변경 불가(immutable)
print("튜플: ", (10,20,30,20,30))
print("튜플: ", ("A","B","C"))
print("튜플: ", tuple()) #empty tple
num2 = (90,80,70,60,50)
print(num2[0])
# num2[0] = 100  #값변경 불가

# 단 하나의 값만 가질 tuple 표현
x = (10,)
print("10만 저장:",x,type(x)) #<class 'tuple'>
x2 = (10)
print("10만 저장:",x2,type(x2)) #<class 'int'>

# 4.셋(set) : 순서가 없고 중복 불가(한번만 저장), immutable 값만 저장 가능
print("셋: ", {10,20,30,20,30})
print("셋: ", {"A","B","C"})
print("셋: ", {(10,20)}) # 튜플은 immutable값이라 저장 가능
#print("셋: ", {[10,20]}) 리스트는 mutable값이라 저장 불가

# 5. 딕셔너리(dict) : key/value 쌍으로 저장, 저장순서 없음, 값 변경 가능
print("딕셔너리:", {"name":"홍길동","age":20, "address":"부산"})
