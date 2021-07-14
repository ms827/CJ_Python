'''
    셋(set)
    1. {값, 값2} 표현
    2. 순서가 없고 중복불가
    3. set() 함수
    4. 저장되는 데이터는 immutable값만 저장 가능.
      예> 상수, 문자열, tuple
        list는 저장 불가
'''
#print(dir(set))
'''
add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
'''
# set 함수
int_set = {10,20,30,20,30,99}
print("1. 길이:", int_set, len(int_set))
print("2. 멤버쉽 연산자:", 10 in int_set)

# 1. 값 추가
int_set.add(100)
int_set.add("홍길동")
int_set.add((5,243))
#int_set.add([5,243]) #리스트 저장 불가
print(int_set)

# 2.병합 (update)
n = {54,2,1,4}
n.update({78,3,2})
n.update([88,99,66]) #리스트를 분해후 병합하기 때문에 저장 가능
n.update((10,20,30))
n.update("hello")
print(n)

# 3. 삭제 (discard, remove, pop)
m = {9,8,7,6,5,4,3}
m.pop() # 맨 뒤에 값 삭제
m.remove(9) # 일치하는 값이 없으면 keyError 에러가 발생
m.discard(8) # 일치하는 값이 없으면 do nothing
m.clear() # set() : empty set
print(m)

# 4. 함수를 이용한 교집합, 차집합, 합집합
m = {1,2,3}
m2 = {2,3,5,6}
print(m.union(m2)) #합집합 {1, 2, 3, 5, 6}
print(m.intersection(m2)) #교집합 {2, 3}
print(m.difference(m2)) #차집합 {1}
print(m.symmetric_difference(m2)) #대칭차집합 {1, 5, 6}

# 4. set 연산자를 이용한 교집합, 차집합, 합집합
m = {1,2,3}
m2 = {2,3,5,6}
print(m | m2) # union 동일 {1, 2, 3, 5, 6}
print(m & m2) # intersection 동일 {2, 3}
print(m - m2) # difference 동일 {1}
print(m ^ m2) # symmetric_difference 동일 {1, 5, 6}
