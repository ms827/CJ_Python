# 1. resource/review.txt 읽기
# 경로지정: .(현재디렉토리)   ..(상위디렉토리)
'''
'buffer', 'close', 'closed', 'detach', 'encoding', 'errors',
'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name',
'newlines', 'read', 'readable', 'readline', 'readlines',
'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable',
'write', 'write_through', 'writelines']

'''
# 1. txt파일에 첫 줄 읽기
try:
    with open("./resource/review.txt","r",encoding="utf-8") as f: # 자동으로 close()
        data = f.readline()
        print(data)
except Exception as e:
    print("예외발생:", e)

print("end(정상종료)")
print("#####################################################")
print("#####################################################")
# 2. txt파일에서 통문자(str) 한꺼번에 읽기
try:
    with open("./resource/review.txt","r",encoding="utf-8") as f: # 자동으로 close()
        data = f.read()
        print(data,type(data))
except Exception as e:
    print("예외발생:", e)

print("end(정상종료)")
print("#####################################################")
print("#####################################################")
# 3. txt파일에서 list로 한꺼번에 읽어서 한줄 씩 출력
try:
    with open("./resource/review.txt","r",encoding="utf-8") as f: # 자동으로 close()
        data = f.readlines()
        for line in data:
            print(line, end="")

except Exception as e:
    print("예외발생:", e)

print("end(정상종료)")
print("#####################################################")
print("#####################################################")
# 4. txt파일에서 list로 한꺼번에 읽어서 한줄 씩 출력
try:
    with open("./resource/review.txt","r",encoding="utf-8") as f: # 자동으로 close()
        for line in f:
            print(">>",line,end="")

except Exception as e:
    print("예외발생:", e)

print("end(정상종료)")
