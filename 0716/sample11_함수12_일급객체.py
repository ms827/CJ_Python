'''

  *일급객체(first-class): python, javascript
    --> 함수를 데이터로 처리
      가. 함수를 변수에 저장 가능하다.
      나. 함수를 호출할 때 인자값으로 함수를 사용할 수 있다
      다. 함수의 리턴값으로 함루를 사용할 수 있다.

        ==> 함수명() 아닌 함수명만 사용해서
            특정시점에 () 붙여서 실행하게 할 수 있다.

            시점
             -시스템이 필요에 의해서 호출 (콜백 : callback)
             -사용자에 필요에 의해서 호출
'''

def fun1():
    print("fun1")

print(fun1) # <function fun1 at 0x000002121D7C2790> #()붙이면 실행 안붙이면 주소값을 보인다
fun1()
# fun1 = 100
# fun1()  #더이상 fun1은 함수가 아니기때문에 저장을 할수가 없다.

# 가. 함수를 변수에 저장 가능하다.
new_fun = fun1
new_fun()

# 나. 함수를 호출할 때 인자값으로 함수를 사용할 수 있다.
def fun2(f):
    f()

fun2(fun1)


# 다. 함수의 리턴값으로 함루를 사용할 수 있다.
def fun3():
    return fun1

result = fun3()
result()