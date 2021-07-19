#sample01.py
#module01.py를 접근하는 모듈이다.

# 가) import 패키지명, 모듈명
import sample01_package.module01
import sample01_package.module02




# 관례적으로 시작점 지정
#print("sample01>>>>>",__name__)
if __name__ == "__main__":
    print(sample01_package.module01.num)
    sample01_package.module01.fun1()
    p = sample01_package.module01.Person()

    print(sample01_package.module02.size)