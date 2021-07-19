#sample03.py
#module03.py를 접근하는 모듈이다.

from sample01_package.module01 import num, fun1, Person
from sample01_package.module02 import size


# 관례적으로 시작점 지정
#print("sample01>>>>>",__name__)
if __name__ == "__main__":
    print(num)
    fun1()
    p = Person()

    print(size)