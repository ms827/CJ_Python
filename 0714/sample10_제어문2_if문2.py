'''
    문장(statement)

    실행문
        가. 순차문
        나. 제어문 - 조건문: 단일 if문, if~else문, 다중 if문, 3항 연산자
                    반복문: for문, while문

        *주의할 점은 반드시 들여쓰기 사용해야 한다.

    비실행문 - 주석문( 한줄 주석문, 멀티 주석문)
'''

#2. if~else문
# 조건에 따라서 실행문장이 달라진다.
'''
문법:
    if 조건식: 조건식에 사용 가능한 연산자? 비교연산자, 논리연산자, 멤버쉽연산자, isNone
        문장1    # 조건식이 True인 경우에 실행
    else:
        문장2    # 조건식이 False 인 경우에 실행
'''
print("1")
if True:
    print("True")
else:
    print("False")
print("end")

#문제: 키보드로 숫자를 입력 받아서 짝수면 "짝수" 홀수면 "홀수" 출력
num = input("숫자입력:")

if int(num)%2==0:
    print("짝수")
else:
    print("홀수")
print("end")


#문제2: 제공된 리스트에서 정수 10이 존재하면 "값이 있음" 없으면 "None"출력
num_list=[10,20,30]

if 10 in num_list:
    print("값이 있음")
else:
    print("None")
print("end")