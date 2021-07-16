# 학생 관리 프로그램 개발
'''
    1. 분석단계
      학생객체
        - 속성: 학번,이름,나이
        - 동작: pass

    2. 설계단계
      학생객체 ---> 학생 클래스
      속성    ---> 변수
      동작    --->메서드

    ex> 설계도 틀 (클래스) ----->건물(인스턴스) 여러개
'''
class Student:
    # 생성자 (생성자 함수)
    def __init__(self,n,n2,n3): #로컬변수 #self는 생략가능 개수에 포함x
        print(id(self))
        #인스턴스 변수
        self.ssn = n
        self.name = n2
        self.age = n3

#학생클래스를 객체생성할 때 속성값(이름,나이,학번)을 저장할 수 있다.
stu1 = Student("A01","홍길동",20)
print(id(stu1))
print(stu1.ssn)
print(stu1.name)
print(stu1.age)

