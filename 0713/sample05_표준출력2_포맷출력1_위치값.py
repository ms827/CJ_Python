'''
표준출력 + 포맷지정
1.print(" ... {}, ...{}".format(   값,  값1) )
'''

name = "홍길동"
age = 20

# 1.권장하지 않는 방법
#출력 포맷 ? 이름:홍길동, 나이:20
print("이름:"+name +",   나이:" + str(age) )

# 2. "".format 함수
print("이름:{0}, 나이:{1}".format("홍길동",20))
print("이름:{}, 나이:{}".format("홍길동",20))
print("이름:{1}, 나이:{0}".format("홍길동",20))
print("이름:{0:10s}, 나이:{1}".format("홍길동",20)) #10s 열자리 str로 표현
