'''
    문장(statement)

    실행문
        가. 순차문
        나. 제어문 - 조건문: 단일 if문, if~else문, 다중 if문, 3항 연산자
                    반복문: for문, while문

        *주의할 점은 반드시 들여쓰기 사용해야 한다.

    비실행문 - 주석문( 한줄 주석문, 멀티 주석문)
'''

#1. 단일 if문
# print("2") 문장을 조건에 따라서 실행(조건이 True)하거나 실행하지 않게(조건이 False) 처리
'''
문법:
    if 조건식: 조건식에 사용 가능한 연산자? 비교연산자, 논리연산자, 멤버쉽연산자, isNone
        문장
'''
print("1")
if True:
    print("2")
print("3")
print("4")

if 3==3:
    print("실행1")
if 3>4 or 4==4:
    print("실행2")
if []is  not None:
    print("실행3")
if 10 in [10,203]:
    print("실행4")

if True:
    pass

#권장 안함
if 3==3: print("실행5")
print("end")