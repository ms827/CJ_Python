'''
    분석단계
    1. 고양이 관리 프로그램 ==> 고양이 객체 추출
    2. 속성 : 이름, 나이, 성별
    3. 동작 추출 : 먹기,울기

    설계단계
    1)고양이 객체 ==> 고양이 클래스
    2)속성 ===> 인스턴스 변수
    3)동작 ===> 메서드
'''
class Cat:

    def __init__(self,name,age,sex): #생성자
        #인스턴스변수
        self.name = name
        self.age = age
        self.sex = sex

    # 매서드(기능처리 담당)
    def eat(self):
        print(self.name,"cat.eat")

    def cry(self):
        print(self.name,"cat.cry")

cat1 = Cat("야옹이",2,"암컷")
print("이름:{} 나이:{} 성별:{}".format(cat1.name, cat1.age, cat1.sex))
cat1.eat()
cat1.cry()


