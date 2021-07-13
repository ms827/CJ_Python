#대입연산자 심화

#1.동시에 변수 할당
n=n2=n3=100
print(n,n2,n3)

#2.여러값을 동시에 여러 변수에 저장가능(변수와 값의 갯수가 일치)
name,age,address="홍길동", 20, "서울" #tuple동일
print(name,age,address)

#Q 다음 중 변수값을 change하시오
v1, v2 = 100, 200
print(v1,v2)
v1,v2 = v2,v1
print(v1,v2)

#dict는 key값이 저장됨
x,x2 = {"username":"홍길동", "age":20}
print(x,x2) #username age

#변수와 값의 갯수가 일치하지 않아도 가능한 방법
#packing
n,*n2 = 10, 20, 30 # 10 [20, 30]
print(n, n2)

*n,n2 = 10, 20, 30 # [10, 20] 30
print(n, n2)

n,*n2 = [10, 20, 30] # 10 [20, 30]
print(n, n2)

x,*x2 = {"username":"홍길동", "age":20, "address":"서울"}
print(x,x2) #username ['age', 'address']