'''
    파일 사용 ( 입력/출력)
    1.사용하겠습니다. --> open()
    2.사용 (읽기/쓰기)
    3.잘 사용했습니다. --> close()

'''

# 1. resource/review.txt 읽기
# 경로지정: .(현재디렉토리)   ..(상위디렉토리)
f = None
try:
    f = open("./resource/review.txt","r")
    print(f)
except Exception as e:
    print("예외발생:",e)
finally:
    if f is not None:
        f.close()
print("end(정상종료)")