'''
    문자열 종류
    1. 유니코드 표현
      --> 일반적으로 사용되는 표현

    2. byte 표현
      --> 네트워크 이용해서 가져왔을 때

    3. 서로 변환 작업 필요

'''

# 1. bytes 표현 (binary 표현식)
n = b'abcde'
print(n,type(n))

n2 = 'abcde'
print(n2, type(n2))

# 2. 변환
s = "abcde 안녕하세요"
s_bytes = s.encode('utf-8')
print("bytes로 변환:", s_bytes)

s_uni = s_bytes.decode('utf-8')
print("unicode로 변환:", s_uni)

