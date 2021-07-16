'''
    문장(statement)

    실행문
        가. 순차문
        나. 제어문 - 조건문: 단일 if문, if~else문, 다중 if문, 3항 연산자
                    반복문: for문, while문

        *주의할 점은 반드시 들여쓰기 사용해야 한다.

    비실행문 - 주석문( 한줄 주석문, 멀티 주석문)
'''

#1. for문
'''
문법:
for 변수 in iterable객체: # iterable객체는 집합형 형태(문자열,리스트,튜플,셋,딕셔너리) 형태이다
    문장
    
'''
#1. 문자열
for n in "hello":
    print("A:", n)
print("end")

for idx,n in enumerate("hello"):
    print("B:", idx, n)
print("end")

for idx,n in enumerate("hello", start=10):
    print("C:", idx, n)
print("end")


#2. 리스트

for n in [10,20,30]:
    print("D:", n)
print("end")

for idx,n in enumerate([10,20,30]):
    print("D1:", idx, n)
print("end")

for idx,n in enumerate([10,20,30], start=1):
    print("D2:", idx, n)
print("end")

#3. 튜플

for n in (10,20,30):
    print("E:", n)
print("end")

for idx,n in enumerate((10,20,30)):
    print("E1:", idx, n)
print("end")

for idx,n in enumerate((10,20,30), start=1):
    print("E2:", idx, n)
print("end")

#4. 셋(순서없고 중복불가)

for n in {10, 20, 30}:
    print("F:", n)
print("end")

for idx,n in enumerate({10, 20, 30}):
    print("F1:", idx, n)
print("end")

for idx,n in enumerate({10, 20, 30}, start=1):
    print("F2:", idx, n)
print("end")
