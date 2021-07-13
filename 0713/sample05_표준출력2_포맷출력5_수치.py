'''
수치데이터 포맷 + 옵션

"{:옵션}".format(수치값}

'''

print("{0}".format(12345)) #12345
print("{0:f}".format(12345)) #12345.000000
print("{:f}".format(12345)) #12345.000000
print("{0:.2f}".format(12345)) #12345.00

print("{0:,}".format(123456789)) #123,456,789

#진수표기
print("int:{0}, bin:{0:b}, oct:{0:o}, hex:{0:x}".format(10)) #int:10, bin:1010, oct:12, hex:a