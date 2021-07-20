'''
    sample.txt 읽어서
    각 과목의 총점 및 평균 출력
'''
kor_sum=[]
eng_sum=[]
math_sum=[]
try:
    with open("./resource/sample.txt","r",encoding="utf-8") as f:
        header = f.readline()
        while True:
            data = f.readline()
            if not data: break
            kor,eng,math = data.split(",") # [70,60,88]
            kor_sum.append(int(kor))
            eng_sum.append(int(eng))
            math_sum.append(int(math))
except Exception as e:
    print("예외발생:", e)

print(" 국어 총점 : {} 평균 : {}".format(sum(kor_sum),sum(kor_sum)/len(kor_sum)))
print(" 영어 총점 : {} 평균 : {}".format(sum(eng_sum),sum(eng_sum)/len(eng_sum)))
print(" 수학 총점 : {} 평균 : {}".format(sum(math_sum),sum(math_sum)/len(math_sum)))