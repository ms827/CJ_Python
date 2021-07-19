#sample02.py
#module02.py를 접근하는 모듈이다.

from sample01_package import module01,module02



# 관례적으로 시작점 지정
#print("sample01>>>>>",__name__)
if __name__ == "__main__":
    print(module01.num)
    module01.fun1()
    p = module01.Person()

    print(module02.size)
