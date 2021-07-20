'''
    sample.json 읽기
'''
import json

try:
    with open("./resource/sample.json",mode="r",encoding="utf-8") as f:
        while True:
            row = f.readline()
            if not row: break
            json_format = json.loads(row)
            #print(json_format.keys())
            for key,value in json_format.items():
                print(key, value)
except Exception as e:
    print("Error:",e)

print("end")

