'''
    문자열 색인 종류
    1. 인덱싱
        --> 하나를 참조
        --> 문자열[index]
    2. 슬라이싱
        --> 범위 참조
        --> 문자열[start위치:end위치]
            start위치는 생략가능하다. 0부터 시작
            end위치는 생략가능하다. 끝까지, (exclusive,포함 안됨)
            s[:] 는 0부터 끝까지 색인

    색인 방법 --> 위치값(index, 첨자)이용
    -5 -4 -3 -2 -1
     H  e  l  l  o
     0  1  2  3  4 (순방향)
'''

s = "대한민국"

#1. 인덱싱
print(s[0], s[1]) # 대 한
print(s[-1], s[-2]) # 국 민

#2. 슬라이싱
print(s[0:3]) # 대한민 (end는 지정된 값 전까지)
print(s[:3]) # 대한민
print(s[1:3]) # 한민
print(s[1:]) # 한민국
print(s[:]) # 대한민국

print(s[-3:-1]) # 한민
print(s[-3:]) # 한민국

s = "helloworld"
print(s[::2]) # hlool
print(s[1:8:2]) # elwr
# 거꾸로
print(s[::-1]) # dlrowolleh
