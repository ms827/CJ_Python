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

3. 모든 클래스의 최상위 클래스: object

'''

class Pet:  # class Pet(object) : 동일
    pass

class Cat(Pet):
    pass

class Dog(Pet):
    pass

###################
print("상속관계의 계층구조 확인:", Cat.mro())
print(dir(object))

