#집합형 데이터 종류 및 표현

#1.문자열
print("문자열: ", '안녕하세요')
print("문자열: ", "안녕하세요")
print("문자열: ", '''안녕하세요''')
print("문자열: ", """안녕하세요""")

#한줄 주석

'''
멀티 라인 주석
'''

#2. 이스케이프 문자 (escape)
print("He\"llo") # He"llo
print("He\'llo") # He'llo
print("He'llo") # He'llo
print("c:\\aaa") # c:\aaa
print("c:\taaa") # c:	aaa
print("c:\naaa") #엔터친 효과

#3. 이스케이프 문자 비활성화 ==> raw string
print(r"He\"llo") # He"llo
print(r"He\'llo")
print(r"c:\\aaa")
print(r"c:\taaa")

# 파일 경로 지정방법 2가지
print("c:\\bbb")
print(r"c:\\bbb") #권장