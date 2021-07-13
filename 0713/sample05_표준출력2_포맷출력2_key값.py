'''
표준출력 + 포맷지정
2.print(" ... {key}, ...{key2}".format(   key=값,  key2=값) )
3.print(" ... {key}, ...{0}..{1}".format(값2, 값3, key=값 ) )

'''

#2. "".format 함수
print("이름:{username}, 나이:{age}".format(username="홍길동",age=20))
print("이름:{username}, 나이:{age}, 주소:{0}".format("서울", username="홍길동",age=20))

