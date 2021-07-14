'''
    리스트 함수
'''
#print(dir(list))
'''
'append', 'clear', 'copy', 'count', 'extend', 
'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
'''

int_list = [10,20,30,40]

print("1. 리스트 길이:",len(int_list)) # 4
print("2. 추가(맨뒤에)")
int_list.append(50)
int_list.append([5,3]) # 집합형 자체로 저장
int_list.append((5,3))
print(int_list) # [10, 20, 30, 40, 50, [5, 3], (5, 3)]
print("3. 삽입")
int_list.insert(0,100)
int_list.insert(0,[5,4,3])
print(int_list)

print("4. 병합")
int_list = [10,20,30,40]
#int_list.extend(10) 집합형이 아닌 기본형이라 에러
int_list.extend([10,20]) #리스트 안에있는 값이 저장
int_list.extend("Hello")
int_list.extend((33,))
print(int_list) # [10, 20, 30, 40, 10, 20, 'H', 'e', 'l', 'l', 'o', 33]
x = [10,20]
x2 = [4,3]
print(x+x2) #병합효과 [10, 20, 4, 3]

print("5. 특정위치")
int_list=[10,20,30,40]
print(int_list.index(30)) #2
#print(int_list.index(99)) #ValueError, 지정된 값이 없으면 에러

print("6. 거꾸로 - 원본이 거꾸로 변경")
int_list=[10,20,30,40]
int_list.reverse()
print(int_list)
print("6. 거꾸로 - 원본유지하고 거꾸로된 복사본 반환")
int_list=[10,20,30,40]
copy_list = reversed(int_list)
print("원본:", int_list)
print("복사본:", list(copy_list))

print("7. 삭제 - clear,pop,remove")
int_list=[10,20,30,40]
int_list.pop(0) # 위치로 삭제
int_list.pop()  # pop(-1) 동일
print(int_list)

int_list.remove(20) # remove(값)
print(int_list)

int_list.clear() # 전체 삭제
print(int_list) # []

print("8. 복사 - copy(), [:], list()")
int_list=[10,20,30,40]
copy_list = int_list.copy()
copy_list = int_list[:] # copy와 동일한 효과
copy_list = list(int_list) # copy와 동일한 효과
print(int_list == copy_list) # True
print(int_list is copy_list) # False

print("9. 정렬 - 자신이 정렬(in-place)")
num = [8,5,66,22,6,1,486]
num.sort()
num.sort(reverse=True)
print(num)
print("9. 정렬 - 복사본")
copy_num = sorted(num)
copy_num = sorted(num,reverse=True)
print("원본:",num)
print("복사본:", copy_num)

print("10. 정렬 심화")
str_num = ['10','6','3','337','55']
str_num.sort(key=int)
str_num.sort(key=int,reverse=True)
print(str_num)

str_name = ["홍길동","세종","박혁거세","홍"]
str_name.sort(key=len)
print(str_name)