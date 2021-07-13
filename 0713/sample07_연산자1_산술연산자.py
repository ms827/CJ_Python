#산술연산자

n=10
n2=3

print(n+n2) #13
print(n-n2) #7
print(n*n2) #30
print(n/n2) #3.3333333333333335
print(n%n2) #1
print(n//n2) #3
print(n**n2) #1000

#몫과 나머지를 한꺼번에 반환 ==> divmod(10,3)
result = divmod(10,3)
print(result) #(3, 1) 튜플로 반환
x, x2 = divmod(10, 3)
print(x,x2)