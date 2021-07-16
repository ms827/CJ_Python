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
#5. 딕셔너리
person = {"username":"홍길동","age":20,"address":"부산"}

for n in person:
    print("A:",n, person[n])
print("end")

result = person.keys()
print(result)

for n in person.keys():
    print("B:",n, person[n])
print("end")

for n in person.values():
    print("C:",n)
print("end")

result = person.items()
print(result)

for k, v in person.items():
    print(k,v)
print("end")

