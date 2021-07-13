# 1. int로 변환 --> int(값)

print(int(3.5)) # 3
print(int(-3.5)) # -3
print(int(True)) # 1
print(int(False)) # 0
print(int("10")) # 10
#print(int("aaa")) # ValueError
print(int("      10  ")) # 10  공백무시
print("*"*50)

#2. float로 변환 --> float(값)
print(float(10)) # 10.0
print(float(-10)) # -10.0
print(float(True)) # 1.0
print(float(False)) # 0.0
print(float("123.567")) # 123.567

#3. 논리값(True/False) 변환 --> bool(값)
print(bool(0))
print(bool(''))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(10))
print(bool('aasdf'))
print(bool([1,2]))
print(bool((10,3)))
print(bool({"name":"홍길동"}))


#4. 문자열 --> str(값)
print(str(123)) # "123"
print(str(12.553)) # "12.553"
print(str(True)) # "True"

#5. 아스키코드 --> 문자, 문자 --> 아스키코드값
print(ord('a'),ord('A')) # 97 65
print(chr(97),chr(65)) # a A