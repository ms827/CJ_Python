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
        모든 제어문은 서로간에 중첩이 가능하다
        *주의할 점은 반드시 들여쓰기 사용해야 한다.

    비실행문 - 주석문( 한줄 주석문, 멀티 주석문)

    * range함수
    -->자동으로 지정된 정수값의 갯수 만큼 리스트를 생성해주는 함수이다
'''

result = list(range(10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(range(1,11)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(range(1,11,2)) #[1, 3, 5, 7, 9]
print(result)

#"hello" 5번 출력
for n in range(5):
    print("hello")

# _ : dummy variable
for _ in range(5):
    print("world")

# 중첩 for문
'''
    2 * 1 = 2
    2 * 2 = 4
    2 * 3 = 6
    ..
    4 * 1 = 4
    ..
    9 * 9 = 81
'''

for a in range(2,10):
    for b in range(1,10):
        print("{} * {} = {}".format(a, b, (a*b)))