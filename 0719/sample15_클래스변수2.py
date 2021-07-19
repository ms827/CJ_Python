'''
    클래스 변수 (class variable)

    1. 클래스 구성요소

        class Person:
            생성자(메서드) : def __init__(self) 매직메서드 사용
            인스턴스변수 : self.변수명 형식으로 사용, 생성자 또는 메서드 내에서 사용함.
            클래스변수  : 메서드 밖에서 self 없이 선언하고
                        사용할 때는 반드시 클래스명.클래스변수 형식으로 사용한다
                        프로그램 실행시 생성 ~ 프로그램 종료시 삭제
            메서드     : def 메서드명(self) 메서드 형식
    2. 클래스변수 용도
      - 프로그램 실행시 생성되서 프로그램 종료시 제거되기 때문에 가장 오래 메모리에 남아있다. + 한번만 생성된
       => 누적용

'''
# 실습 : Person 클래스를 몇번 객체생성했는지를 카운트 하자.
class Person:
    count = 0
    def __init__(self,name):
        self.name = name
        Person.count += 1

p = Person("홍길동")
print(Person.count)
p2 = Person("이순신")
print(Person.count)
