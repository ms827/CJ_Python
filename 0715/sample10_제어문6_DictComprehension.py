'''
    List comprehension
    1. for문 활용
    2. 용도:
            1) dict를 반복해서 가공한후 최종적으로 dict에 저장해서 반황하는 방법.
            2) dict를 반복해서 가공한후 조건(단일 if문)에 맞은 값만 최종적으로 dict에 저장해서 반환하는 방법.
            2) dict를 반복해서 가공한후 조건(if~else문:3항연산자)에 맞은 값만 최종적으로 dict에 저장해서 반환하는 방법.

    3. 1)문법
        변수 = { 연산식 for 변수 in dict.items() }
        변수 = { k:v for k,v in dict.items() }


        2)문법
        변수 = { k:v for k,v in dict.items() if 조건식}


        3)문법
        변수 = { 3항연산자 k:v for k,v in dict.items() }
        변수 = { 참 if 조건식 else 거짓 for k,v in dict.items() }

'''

m = {"a":10,"b":20,"c":43}
#dict의 값을 +10 해서 dict로 반환하시오
m2 = {k:v+10 for k,v in m.items()}
print(m2)

#dict의 k와 v를 바꾸시오
m3 = {v:k for k,v in m.items()}
print(m3)

#a와 b만 반환
m = {"a":10,"b":20,"c":43}
m2 = {k:v+10 for k,v in m.items() if k!="c"}
print(m2)

#a는 값 +10 나머지는 값-10
m = {"a":10,"b":20,"c":43}
m2 =  { k:v+10 if k=="a" else v-10 for k,v in m.items() }
print(m2)