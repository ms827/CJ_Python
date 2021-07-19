'''
    클래스 변수 (class variable)

    1. 클래스 구성요소

        class Person:
            생성자(메서드) : def __init__(self) 매직메서드 사용
            인스턴스변수 : self.변수명 형식으로 사용, 생성자 또는 메서드 내에서 사용함.
            클래스변수  : 메서드 밖에서 self 없이 선언하고
                        사용할 때는 반드시 클래스명.클래스변수 형식으로 사용한다
            메서드     : def 메서드명(self) 메서드 형식

'''
class Person:
    age = 10  # 클래스 변수 ( 클래스정보만 저장하는 메모리(method area), 프로그램실행시 생성 ~ 프로그램 종료시 삭제, 1번만 생성된
    def __init__(self, name): # 생성자 # name은 로컬변수(메서드 안에서 선언, stack메모리, 메서드 호출시 생성 ~ 종료시 삭제)
        self.name = name # 인스턴스변수 # self.name은 인스턴스 변수 ( heap메모리, 객체생성시 생성 ~ 객체소멸시 삭제)
        print(Person.age)

    def get_name(self): # 메서드
        return self.name

p = Person("홍길동")
print(p.name)
print(p.get_name())
print(Person.age)