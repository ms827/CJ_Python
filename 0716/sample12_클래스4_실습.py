'''
    주문?
    1. 애완동물 관리 프로그램 개발
      --> 고양이 관리 프로그램
      --> 속성 : 이름, 나이, 성별
    2. 실제 고양이 정보
      1) "야옹이" 2 암컷
      2) "망치" 1 숫컷
    3. 출력
        이름 : 야옹이 나이 : 2 성별 : 암컷
'''

class Pet: # 클래스
    def __init__(self,n,n2,n3):  #생성자 #self = 인스턴스 주소값
        #인스턴스 변수
        self.name = n #로컬변수
        self.age = n2 #로컬변수
        self.sex = n3 #로컬변수

pet1 = Pet("야옹이",2,"암컷")
pet2 = Pet("망치",1,"숫컷")

print("이름:{} 나이:{} 성별:{}".format(pet1.name, pet1.age, pet1.sex))
print("이름:{} 나이:{} 성별:{}".format(pet2.name, pet2.age, pet2.sex))