'''
    문제1: 주민번호 암호화 하는 함수를 작성하시오
    예> 입력: 991111-1234567
        출력: 991111-1******
'''

def secret(ssn):
    return ssn[:8] + "******"

result = secret(input("주민등록번호:"))
print(result)

'''
    문제2:파일명만 반환하는 함수 작성
      예> 입력:test.py
          출력:test
'''

def name(file):
    return file[:file.find(".")]

result = name(input("파일 이름:"))
print(result)