'''
    named 파라미터
    ==> 함수호출시
        def fun1(name, age):
            pass

        fun1("홀길동",20)
        fun1(name="홀길동", age=20)
        fun1(age=20, name="홍길동"

'''

def fun1(name, age, address = "부산"):
    print(name, age, address)

fun1("홍길동",20,"서울")
fun1(name="홍길동",age=20,address="서울")
fun1(age=20,name="홍길동")