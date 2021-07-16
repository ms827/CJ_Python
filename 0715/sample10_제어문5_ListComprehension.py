'''
    List comprehension
    1. for문 활용
    2. 용도:
            1) 리스트를 반복해서 가공한후 최종적으로 리스트에 저장해서 반황하는 방법.
            2) 리스트를 반복해서 가공한후 조건(단일 if문)에 맞은 값만 최종적으로 리스트에 저장해서 반환하는 방법.
            2) 리스트를 반복해서 가공한후 조건(if~else문:3항연산자)에 맞은 값만 최종적으로 리스트에 저장해서 반환하는 방법.

    3. 1)문법
        변수 = [ 연산식 for 변수 in 집합형]
        num = [ n + 20  for n in [10,20] ]

        2)문법
        변수 = [ 연산식 for 변수 in 집합형 if 조건식]
        num = [ n + 20  for n in [10,20] if n==20]

        3)문법
        변수 = [ 3항연산자 for 변수 in 집합형 ]
        변수 = [ 참 if 조건식 else 거짓 for 변수 in 집합형 ]
        num = [  ]
'''
#num = []
#for n in [10,20]:
#    n2 = n + 20
#    num.append(n2)
#print(num)

num = [ n + 20  for n in [10,20] ]
print(num)

# 1~10 반복시 짝수만 반환
num2 = [ n for n in range(1,11) if n % 2==0]
print(num2)

# 1~10 반복시 짝수면 +1 ,홀수면 -1 반환
num3 = [ n+1 if n%2==0 else n-1 for n in range(1,11)]
print(num3)