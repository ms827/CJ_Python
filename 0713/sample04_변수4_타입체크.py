'''
변수 타입 체크
type(변수)
'''

int_value = 10
float_value = 3.15
bool_value = True
none_value = None


print(int_value, type(int_value)) #<class 'int'>
print(float_value, type(float_value)) #<class 'float'>
print(bool_value, type(bool_value)) #<class 'bool'>
print(none_value, type(none_value)) #<class 'NoneType'>

str_value = "Hello"
list_value = [10,20,30]
tuple_value = (2,3,4)
set_value = {1,2,3}
dict_value = {"name":"홍길동","age":20}

print(str_value, type(str_value)) #<class 'str'>
print(list_value, type(list_value)) #<class 'list'>
print(tuple_value, type(tuple_value)) #<class 'tuple'>
print(set_value, type(set_value)) #<class 'set'>
print(dict_value, type(dict_value)) #<class 'dict'>