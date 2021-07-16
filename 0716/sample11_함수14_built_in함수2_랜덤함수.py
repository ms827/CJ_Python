'''
    랜덤값 반환
    1. import random

'''
import random
#random.seed(1234) #랜덤값 고정
result = random.random()
print("1. 랜덤float", result)

result = random.randint(1,5) # 1<=N<=5
print("2. 랜덤 범위 int", result)
result = random.randrange(1,11,2) # 1 ~ 11 까지 2step
print("2. 랜덤 범위 int", result)

x = ["A","B","C"]
result = random.choice(x)
print("3.choice",result)
random.shuffle(x)
print("4.shuffle",x)