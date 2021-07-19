'''
    클래스 상속 (inneritance)

1. 상속 특징
    - 재사용( 변수, 메서드 ), 생성자 제외
'''

#애완동물 관리 프로그램( 고양이, 강아지)
class Cat:
    def __init__(self,name,age,sex,alias):
        self.name = name
        self.alias = alias # 별칭은 고양이에만 존재하는 속성이라 가정
        self.age = age
        self.sex = sex

    def eat(self):
        print("cat.eat")

    def __str__(self):
        return "이름{}, 나이:{}, 성별:{}, 별칭{}".format(c.name,c.age,c.sex,c.alias)

class Dog:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def swim(self): # 강아지에만 존재하는 기능이라 가정
        print("dog.swim")
    def eat(self):
        print("dog.eat")

    def __str__(self):
        return "이름{}, 나이:{}, 성별:{}".format(d.name,d.age,d.sex)


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