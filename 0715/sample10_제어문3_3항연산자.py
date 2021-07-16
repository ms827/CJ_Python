'''
    문장(statement)

    실행문
        가. 순차문
        나. 제어문 - 조건문: 단일 if문, if~else문, 다중 if문, 3항 연산자
                    반복문: for문, while문

        *주의할 점은 반드시 들여쓰기 사용해야 한다.

    비실행문 - 주석문( 한줄 주석문, 멀티 주석문)
'''

#4. 3항연산자
#https://docs.python.org/3/reference/expressions.html#conditional-expressions
# 조건이 여러개
'''
문법:
  변수 = 참 if 조건식 else 거짓
'''
result = 100 if True else 200
print(result)

#점수를 입력받고 70점 이상이면 "합격" 이하면 "불합격" 출력
num = int(input("점수:"))
result = "합격" if num >= 70 else "불합격"
print(result)

#정수값을 입력받고, 정수값이 10보다 크면 "The Best", 5보다 크면 "Good", 5보다 작으면 "Worst" 출력
num = int(input("정수값 입력:"))
result = "The Best" if num >= 10 else "Good" if num >= 5 else "Worst"
print(result)