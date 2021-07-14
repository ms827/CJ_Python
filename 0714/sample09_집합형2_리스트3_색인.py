'''
    리스트 색인 종류
    1. 인덱싱
        --> 하나를 참조
        --> 리스트[index]
    2. 슬라이싱
        --> 범위 참조
        --> 리스트[start위치:end위치]
            start위치는 생략가능하다. 0부터 시작
            end위치는 생략가능하다. 끝까지, (exclusive,포함 안됨)
            s[:] 는 0부터 끝까지 색인

    색인 방법 --> 위치값(index, 첨자)이용
    -5 -4 -3 -2 -1 (역방향)
     H  e  l  l  o
     0  1  2  3  4 (순방향)

    3.중첩리스트의 색인(*)

'''

num_list = [90,80,70,60,50,40]

print(num_list[0])
print(num_list[1])
print(num_list[-1])
print(num_list[-2])
print("#" * 40)
print(num_list[0:5]) # [90, 80, 70, 60, 50]
print(num_list[:5]) # [90, 80, 70, 60, 50]
print(num_list[:]) # [90, 80, 70, 60, 50, 40]
print(num_list[-4:-1]) # [70, 60, 50]
print("#" * 40)
print(num_list[0:6:2]) # [90, 70, 50]
print(num_list[::2]) # [90, 70, 50]
print(num_list[::-1]) # [40, 50, 60, 70, 80, 90]

# 중첩리스트 색인
num = [[10,11,12,56,7],[9,8,7,89,3]]
# 56 이후값 반환
n = num[0]
print(n)
print(n[3:])

print(num[0][2]) #12
# 8,7,89 반환?
print(num[1][1:4]) # [8, 7, 89]
