'''
    파일 사용 ( 입력/출력)
    1.사용하겠습니다. --> open()
    2.사용 (읽기/쓰기)
    3.잘 사용했습니다. --> close()

    mode
        "r": read
        "w": write(덮어쓰기)
        "a": append(기존값에 추가)

    파일읽기 에서는 파일이 없으면 FileNotFoundError 발생되서 반드시 예외처리가 필요하다
    파일출력 에서는 파일이 없으면 자동으로 생성해주기 때문에 예외처리가 불필요하다

'''
'''
'buffer', 'close', 'closed', 'detach', 'encoding', 'errors',
'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name',
'newlines', 'read', 'readable', 'readline', 'readlines',
'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable',
'write', 'write_through', 'writelines']

'''
with open("./resource/minseok.txt","a",encoding="utf-8") as f: #with문 이용 자동으로 close()
    f.write("hello\n")

print("end")


