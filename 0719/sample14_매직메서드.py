'''
    매직 메서드 (magic method)
    1. 특징
      - 사용자가 직접 호출 가능하지만, 직접 호출하지 않고
        특정 작업에 대해서 시스템이 내부적으로 호출하는 메서드 의미
        사용자가 필요에 의해서 수정할 수 있다.
    2. 매직 메서드 확인
      print(der(객체))
      __매직메서드__(self) 형식으로 되어 있다.

'''

# 1. __init__ 매직메서드 : 객체생성시 시스템이 내부적으로 호출, 일반적으로 생성자라고 부른다
class Person: #자동으로 시스템이 __init__생성

    def __init__(self):
        print("__init__")

p=Person()


class Person2: #자동으로 시스템이 __init__생성

    def __init__(self,name):
        print("__init__",name)

p2=Person2("홍길동")

# 2.__str__ 매직메서드 : 문자열로 변경시킬때 자동으로 호출된다.  str(),print(),format()
class Person3:

    def __str__(self):

        return "__str__"


p = Person3()
print(str(p))
print(p)
print("{}".format(p))


# 3. __fromat__ 매직메서드 : format() 사용시 자동 호출
class Person4:
    def __format__(self, format_spec):
        return "__format__"

p = Person4()
print("{}".format(p))

# 4. __len__ 매직메서드 : len() 사용시 자동 호출
class Person5:

    def __len__(self):
        return 100

p = Person5()
print(len(p))