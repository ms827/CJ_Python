'''
    클래스 메서드 (class method)

    1. 클래스 구성요소

        class Person:
            생성자(메서드) : def __init__(self) 매직메서드 사용
            인스턴스변수 : self.변수명 형식으로 사용, 생성자 또는 메서드 내에서 사용함.
                        반드시 객체생성 한 후에 사용한다.
                        개별적인 속성값 저장용
            클래스변수  : 메서드 밖에서 self 없이 선언하고
                        사용할 때는 반드시 클래스명.클래스변수 형식으로 사용한다
                        프로그램 실행시 생성 ~ 프로그램 종료시 삭제
                        객체생성 없이 사용가능
                        누적용
            메서드(인스턴스 메서드, regular 메서드) :
                    def 메서드명(self) 메서드 형식, 객체생성시 heap메모리에 생성됨.
                    self.메서드 형식으로 사용한다
                    반드시 객체생성 한 후에 사용한다.
            메서드(클래스) : 프로그램 실행시 생성 ~ 프로그램 종료시 삭제
                          클래스명.메서드 형식으로 사용한다
                          객체생성 없이 사용가능

                         @classmethod --> 데코레이터( 자바에서는 어노테이션 이라고 부른다)
                         def 클래스명(cls):
                            pass

    2. 클래스변수 용도
      - 프로그램 실행시 생성되서 프로그램 종료시 제거되기 때문에 가장 오래 메모리에 남아있다. + 한번만 생성된
       => 누적용

    3. 비교정리
      1) self와 s 는 같다
        객체생성시점에 heap메모리에 생성된 인스턴스(주소값)를 갖는다.

      2) cls와 Student
        객체생성과 무관한 프로그램 실행시점에 method area에 생성된 Strdent클래스 정보가 저장된 주소값을 갖는다.

'''
class Student:
    age = 10
    def __init__(self,name):
        print(self)
        self.name = name

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    #regular 메서드(인스턴스 메서드)
    def get_age(self):
        return Student.age # 프로그램 실행시에 먼저 생성되기 때문에

    #class메서드 ==> self 사용불가 ( 생성 전이기 때문에)
    @classmethod
    def class_fun(cls):
        print("class_fun의 cls:",id(cls))
        print(cls.age,Student.age)
        #print(self)

# 객체생성 전에 임의의 동작하는 메서드가 필요할 때 클래스 메서드를 사용한다.
Student.class_fun()

s = Student("홍길동")
print(s)

print("Student 클래스: ",id(Student))
Student.class_fun()