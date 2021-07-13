#논리 연산자
'''
1. 논리 연산자 종류
and : 그리고
or : 또는
not : 부정

2.논리값(True/False) 값만 논리값으로 사용하지 않는다.

가.False가 될수 있는 값
0
''
None
[]
()
{}  : dict

나. 가)이외의 값은 모두 True로 처리된다

--> 확인방법은 bool()함수 또는 not
'''

print("1. False로 처리되는 값")
print(bool(0))
print(bool(''))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))

print("2. True로 처리되는 값")
print(bool(10))
print(bool('abcd'))
print(bool([1,2]))
print(bool((3,4)))
print(bool({"name":"홍길동"}))

print("#" * 40)
print(not 10) #False
print(not 0) #True

print("#" * 40)
#논리값(True/False)이 아닌 값으로 논리연산자(and,or,not) 사용가능

# 가.and : 좌 값이 참이면 우 값을 반환, 좌 값이 거짓이면 좌 값을 반환
# 논리값이 최종적으로 정해지는 값을 반환
print( "123" and 0 ) #0
print( 0 and 123 ) #0

# 나.or : 좌 값이 참이면 좌 값을 반환, 좌 값이 거짓이면 우 값을 반환
# 논리값이 최종적으로 정해지는 값을 반환
print( "123" or 0 ) #123
print( 0 or 123 ) #123

#
