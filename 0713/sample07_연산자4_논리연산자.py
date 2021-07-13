#논리 연산자
'''
and : 그리고
or : 또는
not : 부정
'''

print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False
print("*"*40)
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False
print("*"*40)
print(not True)
print(not False)

# Q? num값이 2보다 크거나 짝수값?
num = 10
print((num > 2) or (num %2 == 0))

