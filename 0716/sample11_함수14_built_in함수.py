'''
    빌트인 함수
'''
print(dir(__builtins__))

'''
'ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 
'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 
'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 
'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 
'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 
'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 
'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 
'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 
'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 
'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 
'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 
'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 
'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', 
'__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 
'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 
'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 
'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 
'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 
'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 
'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

'''

print("1. 합계: ", sum([1,2,3,4,5])) # 15
int_value = [1,2,3,4,5]
print("2. 평균: ", sum(int_value)/len(int_value)) # 3.0
print("3. 최대값, 최소값: ", max(int_value), min(int_value)) # 5 1
str_value = ["121","567","635","599","7","3456"]
print("3. 최대값, 최소값: ", max(str_value, key=int), min(str_value, key=int)) # 3456 7
print("3. 최대값, 최소값: ", max(str_value, key=len), min(str_value, key=len)) # 3456 7
dict_value = {10:"aa",7:"bb",1:"cc"}
print("3. 최대값, 최소값: ", max(dict_value), min(dict_value)) # 10 1
print("4. 절대값: ", abs(10), abs(-10)) # 10 10
print("5. 아스키코드: ", chr(97), ord('A')) # a 65   a:97 A:65
print("6. a몫과 나머지: ", divmod(10,3)) # (3, 1)
print("7. 반올림: ", round(4.67)) # 5, 소수점 0자리에서 반올림해서 정수반환
print("7. 반올림: ", round(4.67, 1)) # 5, 소수점 1자리 반올림
print("8. list변환: ", list("hello")) # ['h', 'e', 'l', 'l', 'o']
print("8. set변환: ", set([10,29,10,45])) # {10, 45, 29}
print("8. tuple변환: ", tuple([10,29,10,45])) # (10, 29, 10, 45)
print("8. dict변환: ", dict(name="홍",age=20)) # {'name': '홍', 'age': 20}
print("8. int변환: ", int("10")) # 10
print("8. str변환: ", str(10) + "값") # 10값
print("8. bool변환: ", bool(10)) # True

print("9. range 변환: ", list(range(1,11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("10. 정렬: ", sorted([10,4,2,6,8,9])) # [2, 4, 6, 8, 9, 10] , 복사본
print("11. 거꾸로: ", list(reversed([10,4,2,6,8,9]))) #  [9, 8, 6, 2, 4, 10] , 복사본
print("12. 길이: ", len("helo") ) #  4
print("13. zip: ", dict(zip(['a','b'],[10,20])) ) # {'a': 10, 'b': 20}
print("13. zip: ", list(zip(['a','b'],[10,20])) ) # [('a', 10), ('b', 20)]

# any, all ==> 제공된 집합형의 값이 모두 참이냐(all), 아니면 하나라도 참이냐(any)?
list_value = [10,True,"hello"]
print("14. 모두 참인가?",all(list_value)) #True
print("14. 참값이 있는가?",any(list_value)) #True
list_value = [10,True,"hello",[]]
print("14. 모두 참인가?",all(list_value)) #False
print("14. 참값이 있는가?",any(list_value)) #True

#응용
print(all([True,True]))
print(all([True,True,False]))

int_value = [9,56,2,1,13,65,85]
#모든 값이 10 이상인가
result_value = [ n>= 10 for n in int_value ]
print(result_value)
print(all([ n>= 10 for n in int_value ])) # False
# 값 중에서 3 이하가 있는가?
print(any([ n <= 3 for n in int_value])) # True

'''
    1. filter 함수
        --> 지정된 집합형에서 조건이 일치하는 값(참인경우)만 반환
    2. map 함수
        --> 지정된 집합형의 값을 임의의 함수로 가공해서 반환
    
'''
def even_check(n):
    return n%2==0

result = list(filter(even_check, range(1,11)))
print(result)

l_even_check = lambda n : n%2==0
result = list(filter(l_even_check, range(1,11)))
result = list(filter(lambda n : n%2==0, range(1,11))) # (***) 람다 사용시 권장방법
print(result)

#문제 : 다음 문자열에서 알파벳문자만 출력하시오
def is_alpha(n):
    return n.isalpha

s_str = "He24ll181o6H98i"
result = list(filter(is_alpha, s_str))
result = list(filter(lambda n : n.isalpha(), s_str))
print(result) # ['H', 'e', 'l', 'l', 'o', 'H', 'i']
print("".join(result)) # HelloHi

######################################################
str_list = ["Abc","EbEc","xYz","S"]
#1. 대문자로 변경
def my_upper(s):
    return s.upper()

result = list(map(my_upper, str_list))
result = list(map(lambda n : n.upper(), str_list))
print(result) # ['ABC', 'EBEC', 'XYZ', 'S']

#2. 문자열 길이 반환
str_list = ["Abc","EbEc","xYz","S"]
def my_len(n):
    return len(n)

result = list(map(my_len,str_list))
result = list(map(lambda n:len(n), str_list))
result = list(map(len, str_list)) # built_in 함수 직접 사용
print(result) #[3, 4, 3, 1]

# 3. 숫자값을 문자열 변환
int_value = [74,256,73]
def change_str(s):
    return str(s)
result = list(map(change_str,int_value))
result = list(map(lambda n : str(n), int_value))
result = list(map(str, int_value))
print(result) # ['74', '256', '73']



