'''
     다.파라미터 변수 없고 리턴값 있는 경우
                def 함수명():
                    문장
                    return 값

                def 함수명():
                    문장
                    return 값,값2  ==> (값,값2) 동일
'''

print("1")

def fun1():
    print("fun1")
    return 100
result = fun1()

def fun2():
    print("fun1")
    return 100,200
result = fun2()

print("end",result) #(100, 200)

x,x2 = fun2()
print(x, x2)
