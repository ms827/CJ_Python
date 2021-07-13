#동시에 변수 할당

num=num2=num3=100
num2=200
print(num,num2,num3)


num=num2=num3=[100, 200, 300]
num2=[8,6]
print(num,num2,num3)

#여러값을 동시에 여러 변수에 저장 가능 (변수와 값의 갯수가 일치)
name,age,address="홍길동", 20, "서울" # 튜플과 동일 ( ) 생략
print(name,age,address)

name,age,address=("홍길동", 20, "서울")
print(name,age,address)

# _ 는 dummy variable(더미변수) 라고 부른다.
name,age,_=("홍길동", 20,"서울")
print(name,age)




