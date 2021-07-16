'''
   나. 파라미터 변수 있고 리턴값 없는 경우
           def 함수명(변수,변수2,..):
             문장
'''

print("1")

def fun1(n,n2):
    print("fun1",n,n2)

fun1(10,20)
fun1("홍","김")
result = fun1([1,2],[4,3])
#fun1(10)  # 갯수 불일치로 에러 발생
print("end", result) # None