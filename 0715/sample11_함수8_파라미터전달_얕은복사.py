'''
    함수 호출시 전달되는 파라미터는 얕은 복사(주소값 복사)로 전달된다.
    따라서 함수에서 전달받은 값을 변경하면 원본이 수정된다
    --> 기본값은 값이 복사(call by value)되어 전달되고
        집합형은 주소값이 전달(call by value referance)된다.

'''

def fun1(n, n2):
    n = 20
    n2[0] = 100

x = 10 #기본값
x2 = [10,20,30] #집합형
print("호출전: ", x, x2) #10 [10, 20, 30]
fun1(x, x2) #얕은복사 (기본)
# fun1(x, x2.copy()) #깊은복사
# fun1(x, x2[:]) #깊은복사
# fun1(x, list(x2)) #깊은복사

print("호출후: ", x, x2) #10 [100, 20, 30]

