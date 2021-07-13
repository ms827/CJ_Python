'''
unpacking
1.dict제외한 집합형의 분해는 *사용한다
2.dict는 **사용한다.
'''

print("홍길동") # "홍길동"
print(*"홍길동") # "홍" "길" "동"
print([10,20,30]) #[10, 20, 30]
print(*[10,20,30]) #10 20 30

print("{}:{}:{}".format(*"홍길동"))
print("이름:{0}, 나이:{1}".format(*["홍길동",20]))

person = {"username":"이순신","age":20}
print("이름:{username}, 나이:{age}".format(**person))