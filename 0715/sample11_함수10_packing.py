'''
    packing 파라미터
        def fun1(*n):
            pass

        fun1(10,20)
        fun1(1,2,23,5)


'''

def fun1(*n):
    print(n)

fun1()
fun1(1,2,3)
fun1("a","b","c")

def fun1(m, *n):  # *은 가장 마지막 변수에만 사용 가능
    print(m, n)

fun1(1,4,5,6)
fun1(1,2,3)
fun1("a","b","c")


#dict
def fun2(**n):
    print(n) # {'name': '홍길동', 'age': 20}

fun2(name="홍길동", age=20) # named parameter

# *,** 혼합
def fun3(x,y, *n, **m):
    print(x,y,n,m) # 1 2 (3, 54, 6) {'name': '홍길동', 'age': 20}

fun3(1,2,3,54,6, name="홍길동", age=20) #