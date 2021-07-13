'''
변수 타입 비교
isinstance(변수, 타입)
'''

int_value = 10
float_value = 3.15
bool_value = True
none_value = None

str_value = "Hello"
list_value = [10,20,30]
tuple_value = (2,3,4)
set_value = {1,2,3}
dict_value = {"name":"홍길동","age":20}

print(isinstance(int_value, int))
print(isinstance(float_value, float))
print(isinstance(bool_value, bool))
#print(isinstance(none_value,NoneType)) None은 is None연산자 사용
print(none_value is None)
print(isinstance(str_value, str))
print(isinstance(list_value, list))
print(isinstance(tuple_value, tuple))
print(isinstance(set_value, set))
print(isinstance(dict_value, dict))
