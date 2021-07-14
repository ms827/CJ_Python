'''
    문장(statement)

    실행문
        가. 순차문
        나. 제어문 - 조건문: 단일 if문, if~else문, 다중 if문, 3항 연산자
                    반복문: for문, while문

        *주의할 점은 반드시 들여쓰기 사용해야 한다.

    비실행문 - 주석문( 한줄 주석문, 멀티 주석문)
'''

#3.다중 if문
# 조건이 여러개
'''
문법:
    if 조건식1: 조건식에 사용 가능한 연산자? 비교연산자, 논리연산자, 멤버쉽연산자, isNone
        문장1    # 조건식이 True인 경우에 실행
    elif 조건식2:
        문장2    # 조건식이 False 인 경우에 실행
    elif 조건식3:
        문장3
    else:
        문장4
'''

'''
문제는 학점을 구한다
num = int(input("점수:"))
90~100: A학점
80~89: B학점
70~79: C학점
나머지: F학점
'''
num = int(input("점수:"))

if num<=100 and num>=90:
    print("A학점")
elif num<=89 and num>=80:
    print("B학점")
elif num<=79 and num>=70:
    print("C학점")
else:
    print("F학점")

if 90 <= num <=100:
    print("A학점")
elif 80 <= num <=89:
    print("B학점")
elif 70 <= num <=79:
    print("C학점")
else:
    print("F학점")


if num>=90:
    print("A학점")
elif num>=80:
    print("B학점")
elif num>=70:
    print("C학점")
else:
    print("F학점")
