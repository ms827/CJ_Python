'''
   1. 문자열 생성
'''
m1 = 'hello'
m2 = "hello"
m3 = '''hello'''
m4= """hello"""
print(m1,m2,m3,m4)

# triple 사용 용도1
"""
 멀티 라인 주석
"""

x = "asdfasdfasdfasdfasfdasfdfasdfasdfasdfa" \
    "sfdasfdfasdfasdfasdfasfdasfdfasdfasdfasdfasf" \
    "dasfdfasdfasdfasdfasfdasfdfasdfasdfasdfasfdasfdfasd" \
    "fasdfasdfasfdasfdfasdfasdfasdfasfdasfdfasdfasdfasdfas" \
    "fdasfdfasdfasdfasdfasfdasfdfasdfasdfasdfasfdasfdfasdfas" \
    "dfasdfasfdasfdfasdfasdfasdfasfdasfdfasdfasdfasdfasfdasfdfas" \
    "dfasdfasdfasfdasfdfasdfasdfasdfasfdasf"
print(x)
x2 = """asdfasdfasdfasdfasfdasfdfasdfasdf
asdfasfdasfdfasdfasdfasdfasfdasfdfasdfasdf
asdfasfdasfdfasdfasdfasdfasfdasfdfasdfasdfasdfas
fdasfdfasdfasdfasdfasfdasfdfasdfasdfasdfasfdasfdfasd
fasdfasdfasfdasfdfasdfasdfasdfasfdasfdfasdfasdfasdfasfdas
fdfasdfasdfasdfasfdasfdfasdfasdfasdfasfdasfdfasdfasdfasdfasfdas
fdfasdfasdfasdfasfdasfdfasdfasdfasdfasfdasf"""
print(x2)


html = """
  <html>
    <head></head>
    <body>
      <p>Hello</p>
    </body>
   </html>
"""
print(html)