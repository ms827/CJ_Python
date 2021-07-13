'''
표준출력
1.모니터로 출력
2.print() 함수 사용
3.특정 함수의 사용 방법 알아보기
    help(함수명)
'''
help(print)

# 1.값을 한꺼번에 여러개 출력
print(10, 20, 30) #10 20 30, 공백으로 자동 구분

# 2.sep='' 재정의 가능
print(10, 20, 30, sep=",") # 10,20,30
print(10, 20, 30, sep=":") # 10:20:30
print("#" * 30)

# 3. 기본적으로 print함수는 개행(new line)
print(10)
print(20)
# end='\n' 재정의 가능
print(10, end=" ")
print(20)

# 4.혼합
print(9,8,6, sep=",", end="\n\t")
print(100)
