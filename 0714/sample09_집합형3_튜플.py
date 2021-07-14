'''
    튜플(tuple)
    1. ()표현
    2. 리스트와 동일한 특징
     단, 값 변경 불가 (리스트에서 했던 추가,삽입,삭제,정렬 불가)
    3. tuple(값) 함수
    4. 단 하나의 값을 가진 tuple 표현은?
       (값, )
'''
print(dir(tuple))
'''
 'count', 'index'
'''
#1. tuple 생성 방법
int_tuple = (10,20,30,40)
list_tuple = tuple([10,20,30])
str_tuple = tuple("hello")
print(int_tuple)
print(list_tuple)
print(str_tuple)

# 2. 함수
int_tuple = (10,20,30,40,20)
print("1. 길이:", len(int_tuple)) # 5
print("2. count:", int_tuple.count(20)) # 2
print("3. index:", int_tuple.index(20)) # 1
print("3. index:", int_tuple.index(20,2)) # 4

# 3. 값변경 불가 확인
#int_tuple[0] = 100 #TypeError

# 4. 색인
int_tuple = (10,20,30,40,20)
print(int_tuple[0])
print(int_tuple[-1])
print(int_tuple[1:5])
print(int_tuple[:5])
print(int_tuple[:])
print(int_tuple[::2])
print(int_tuple[::-1])

nested_tuple=((12,3,4,6),(8,7,4,3))
print(nested_tuple[0])
print(nested_tuple[1])
print(nested_tuple[0][1:]) # (3, 4, 6)

#tip
(n, n2, (n3, n4, (n5))) = (1,2,(45,53,(3)))
print(n,n2,n3,n4,n5)

