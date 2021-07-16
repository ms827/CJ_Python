'''
    python 반복문

    1.for문

        for 변수 in 집합형:
            문장

    집합형의 크기만큼 반복된다.

    2.while문

        변수 = 값
        while 조건식:
            문장
            변수증가(감소)

        조건식이 만족하면 반복
        만족하지 않으면 반복 중단

    ex>
        n = 1
        while n < 5:
            pass
            n += 1

    *for vs while
    for문은 반복횟수가 예측이 가능할 때 주로 사용
    while문은 반복횟수가 예측이 어려울 때 주로 사용 (무한반복)

'''

# hello 5번 출력
n = 1
while n<=5:
    print("hello")
    n += 1
print("end")

n = 1
while n<=5:
    print("world")
    if n==3: break #contunue 사용 가능
    n += 1
else:
    print("정상종료")
print("end")