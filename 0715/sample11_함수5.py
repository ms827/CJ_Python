'''
     다.파라미터 변수 없고 리턴값 있는 경우
                def 함수명():
                    문장
                    if 조건식 : return ==> 함수의 기능을 중지
                    문장
                    문장
ㅑ
'''

print("1")

def fun1():
    print("fun1")
    if True: return
    print("fun2")
    print("fun3")

fun1()
print("end")