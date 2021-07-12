print("정수: 0 >>", 0)
print("정수: 양수(10진수) >>", 100) #10
print("정수: 양수(2진수) >>", 0b10) #2
print("정수: 양수(8진수) >>", 0o10) #8
print("정수: 양수(16진수) >>", 0x10) #16
print("정수: 음수 >>", -10) #-10
print("정수: binary함수이용한 2진수 표현>>", bin(2)) #0b10
print("정수: oct함수이용한 8진수 표현>>", oct(8)) #0o10
print("정수: hex함수이용한 16진수 표현>>", hex(16)) #0x10

print("실수: >>", 3.14) #3.14
print("실수:지수표현 >>", 3.14e+5) #314000.0

print("논리: 참 >>", True) #True
print("논리: 거짓 >>", False) #False

#함수
def fun1():
    print("fun1")


print("함수 >>", fun1) #<function fun1 at 0x0000029DB254C0D0> (함수가 저장된 주소값)

print("None: null의미 >>", None) # None
print("None >>", None is None) # True
print("None >>", [10,20] is None) # False


#현재 사용 가능한 함수 출력하기
print(dir("__builtins__"))
'''
['__add__', '__class__', '__contains__', '__delattr__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
  '__hash__', '__init__', '__init_subclass__', '__iter__', 
  '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', 
  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', 
  '__rmul__', '__setattr__', '__sizeof__', '__str__', 
  '__subclasshook__', 'capitalize', 'casefold', 'center', 
  'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
  'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
  'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 
  'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
  'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 
  'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
  'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''











