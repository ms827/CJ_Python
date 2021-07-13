'''
변수 사용
1.목적 : 데이터 저장
2.문법:
    변수명=값
3.변수명 권장은 의미있는 명사형/소문자로 지정
'''

#기본형 데이터를 저장하는 변수 형태
'''
이름""홍길동" 
나이:20
주소:부산
결혼여부: 참/거짓
이메일: aaa@naver.com, aaa@daum.net
핸드폰:010,011
애완동물:강아지,고양이
'''

username = "홍길동"
age = 20
address = "부산"
isMarried = True
email = ["aaa@daum.net","aaa@naver.com"]
options = {
    "phone":["010","011"],
    "pet":["강아지","고양이"]
}

print("이름:", username, id(username))
print("나이:", age, id(age))
print("주소:", address, id(address))
print("결혼여부:", isMarried, id(isMarried))
print("이메일:", email, id(email))
print("추가정보:", options, id(options))