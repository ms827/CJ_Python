'''
    문장(statement)

    실행문
        가. 순차문
        나. 제어문 - 조건문: 단일 if문, if~else문, 다중 if문, 3항 연산자
                    반복문: for문, while문
                        -break문: 반복문을 빠져나올때 사용
                                if 조건식 : break
                        -contuinu문: 반복문 안에서 실행해야 되는 문장들 중에서 일부분을 skip할 때
                        -else문: break아닌 정상적으로 반복문이 종료되었을 때 실행된다
                                즉, break문을 만나서 반복문이 종료되면 실행 안된다.
        *주의할 점은 반드시 들여쓰기 사용해야 한다.

    비실행문 - 주석문( 한줄 주석문, 멀티 주석문)
'''

#1. for문
'''
문법:
for 변수 in iterable객체: # iterable객체는 집합형 형태(문자열,리스트,튜플,셋,딕셔너리) 형태이다
    문장
    
'''
#1. for문

for n in [10,20,30,40]:
    if n == 30: break
    print(n)
print("end")

for n in [10,20,30,40]:
    print("A", n)
    if n == 20: continue
    print("B", n)
    print("C", n)
print("end")

#2. for ~ else문
for n in [10,20,30,40]:
    if n == 30: break
    print("X", n)
else:
    print("정상종료")
print("end")