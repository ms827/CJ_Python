'''
    분석단계
    1. 강아지 관리 프로그램 ==> 강아지 객체 추출
    2. 속성 추출 : 이름, 나이, 성별
    3. 동작 추출 : 먹기, 뛰기

    설계단계
    1)강아지객체 ==> 강아지 클래스 ( 클래스 이름은 첫글자 대문자로 )
    2)속성 ===> 인스턴스 변수 (self.변수명, 생성자 또는 메서드에서 선언되거나 사용된다)
    3)동작 ===> 메서드 ( 반드시 self 파라미터를 가져야 한다. )
'''
class Dog:
    # 생성자(함수) ==> 인스턴스 변수 초기화 역할
    def __init__(self,name,age,sex): # 로컬변수(메서드가 종료되면 제거됨)
        #인스턴스변수 (self.변수 는 삭제x)
        self.name = name
        self.age = age
        self.sex = sex

    # 매서드(기능처리 담당)
    def eat(self):
        print("Dog.eat")
        self.run()
    def run(self):
        print("Dog.run")

    #모든 Dog의 정보를 반환하는 메서드
    def info(self):
        return "이름:{} 나이:{} 성별:{}".format(dog1.name, dog1.age, dog1.sex)

    # __str__(self)함수를 필요에 의해서 수정 ==> 자바는 toString()
    def __str__(self):
        return "이름:{} 나이:{} 성별:{}".format(dog1.name, dog1.age, dog1.sex)

#작성한 클래스를 사용하기 위해서는 반드시 객체생성 필요
dog1 = Dog("망치",2,"숫컷")

print("이름:{} 나이:{} 성별:{}".format(dog1.name, dog1.age, dog1.sex))
dog1.eat()
dog1.run()

print(dog1.info())
print(dog1) # dog1은 실제 Dog 인스턴스의 주소를 가지고 있다. 그런데 print(dog1)했기 때문에
            # 주소값을 문자열로 변환하기 위해서 자동으로 __str__매직 메서드가 호출
            # 매직메서드 특징은 직접 호출하지 않고 특정상황에 자동으로 호출된다
            # 따라서 매직메서드를 사용자 용도에 맞게 수정해서 사용할 수 있다.
print(dog1.__str__())