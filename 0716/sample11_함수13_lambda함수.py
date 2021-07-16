'''
    lambda함수
            가. 파라미터 변수 없고 리턴값 없는 경우
                def 함수명():
                    문장

            나.파라미터 변수 있고 리턴값 없는 경우
                def 함수명(변수1,변수2,...):
                    문장

            다.파라미터 변수 없고 리턴값 있는 경우
                def 함수명():
                    문장
                    return 값

            라.파라미터 변수 있고 리턴값 있는 경우
                def 함수명(변수1,변수2,...
                    문장
                    return 값

'''

# 1. 파라미터 변수 없고 리턴값 없는 경우
def fun1():
    print("fun1, 일반함수")
fun1()

l_fun1 =lambda : print("fun1, lambda")
l_fun1()

# 2. 파라미터 변수 있고 리턴값 없는 경우
def fun2(n,n2):
    print("fun2, 일반함수",n, n2)
fun2(10,20)

l_fun2 = lambda n, n2 : print("fun2, lambda",n, n2)
l_fun2(10,20)

# 3. 파라미터 변수 없고 리턴값 있는 경우
def fun3():
    return 100
result = fun3()
print("fun3, 일반함수",result)

l_fun3 = lambda : 100
result = l_fun3()
print("fun3, lambda함수",result)

# 4. 파라미터 변수 있고 리턴값 있는 경우
def fun4(n, n2):
    return n+n2
result=fun4(10,5)
print("fun4, 일반함수",result)

l_fun4= lambda n, n2 : n+n2
result = l_fun4(10,20)
print("fun4, lambda함수",result)