'''
    unpacking 파라미터
        def fun1(n,n2):
            pass

        fun1(10,20)
        fun1(*[10,20])


'''

def fun1(n, n2):
    print(n, n2)

fun1(10,20)
fun1(*[2,3]) #풀어준후 저장
#fun1(*[2,3,5,7]) # fun1(n, *n2) 일경우 가능