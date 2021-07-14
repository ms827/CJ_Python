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
# dict 함수
m = {"name":"홍길동", "age":20}

# 1. 조회 - key 알고 있다는 전제
result = m["name"]
result = m.get("name")
print(result)
#result = m["email"] # key가 없으면 에러
result = m.get("email") # None
result = m.get("email", "default값") #default 값
print(result)

# 2. 추가 (key가 있으면 세로운 값으로 덮어쓴다(수정) 없으면 새로 생성)
m = {"name":"홍길동", "age":20}
# email 추가
m["email"]="hong@daum.net" #생성
m["age"]=30 #수정
print(m) #{'name': '홍길동', 'age': 30, 'email': 'hong@daum.net'}

# 3. update (병합 : 결국에는 병합되면서 수정됨)
m = {"name":"홍길동", "age":20, "address":"부산"}
m2 = {"name":"이순신", "age":50, "email":"hong"}
m.update(m2)
#m2.update(m)
print(m) #{'name': '이순신', 'age': 50, 'address': '부산', 'email': 'hong'}
print(m2) #{'name': '이순신', 'age': 50, 'email': 'hong'}

# 4. 삭제
m = {"name":"홍길동", "age":20, "address":"부산"}
m.pop("address")
print(m) #{'name': '홍길동', 'age': 20}
m.clear()
print(m) #{}

# 5. 색인
# 가. 모든 key값 얻기
m = {"name":"홍길동", "age":20, "address":"부산"}
result = m.keys()
print("keys: " , list(result)) # keys:  ['name', 'age', 'address']
result = m.values()
print("values: " , list(result)) # values:  ['홍길동', 20, '부산']
result = m.items()
print("items: " , list(result)) #items:  [('name', '홍길동'), ('age', 20), ('address', '부산')]

# 6. etc
m = {"name":"홍길동", "age":20, "address":"부산"}
print("1. dict 길이:",len(m)) # 3
print("2. 멤버쉽 연산자:", "name" in m) # True
print("2. 멤버쉽 연산자:", "email" in m) # False

# 7. 두개의 리스트값을 하나는 key, 다른하나는 value로 묶어서 dict로 변환 (*****)
m = ["대한민국", "미국", "영국"]
m2 = ["서울", "워싱턴", "런던"]
result = zip(m,m2)
print(list(result))
print(dict(zip(m,m2))) #{'대한민국': '서울', '미국': '워싱턴', '영국': '런던'}

# 문제--> {수도:국가, 수도:국가 } 변환
result2 = dict(zip(m,m2))
print(result2)

print(dict(zip(result2.values(),result2.keys()))) #{'서울': '대한민국', '워싱턴': '미국', '런던': '영국'}


