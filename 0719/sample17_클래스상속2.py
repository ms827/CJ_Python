'''
    클래스 상속 (inneritance)

1. 상속 특징
    - 재사용( 변수, 메서드 ), 생성자 제외
2. 상속 방법
  --> 1)여러 클래스들(cat,dog)간의 공통적인 속성과 동작을 추출해서
     여러 클래스들(cat,dog)보다 큰 개념의 클래스를 생성한다
     큰 개념의 클래스(pet)에 공통적인 속성과 동작을 지정한다.
     2) 상속 적용
        class 자식클래스(부모클래스):
            pass

        부모가 가진 속성과 동작을 자식이 그냥 사용가능
'''

#애완동물 관리 프로그램( 고양이, 강아지)
class Pet:
    def __init__(self, name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("pet.eat")

class Cat(Pet): #Pet과 Cat은 상속이된
    def __init__(self,name,age,sex,alias):
        super().__init__(name,age,sex) # name,age,sex는 부모인 Pet에서 선언되었기 때문에 부모에게 전달한다.
        self.alias = alias # alias는 Cat에서 추가된 변수이기 때문에 Cat 자신이 초기화한다.

    def __str__(self):
        return "이름:{}, 나이:{}, 성별:{}, 별칭{}".format(c.name,c.age,c.sex,c.alias)
    # 오버라이딩(overriding) : 부모의 메서드를 자식이 필요에 의해서 재정의 됨
    def eat(self):
        print("cat.eat")

class Dog(Pet):
    def __init__(self, name, age, sex):
       super().__init__(name, age, sex)

    def swim(self): # 강아지에만 존재하는 기능이라 가정
        print("dog.swim")

    def __str__(self):
        return "이름:{}, 나이:{}, 성별:{}".format(d.name,d.age,d.sex)


c=Cat("야옹이",2,"암컷","옹이")
d=Dog("망치",1,"숫컷")

print("고양이 정보")
#print("이름:{}, 나이:{}, 성별:{}, 별칭{}".format(c.name,c.age,c.sex,c.alias))
print(c)
c.eat()
print("강아지 정보")
#print("이름:{}, 나이:{}, 성별:{}".format(d.name,d.age,d.sex))
print(d)
d.eat()
d.swim()