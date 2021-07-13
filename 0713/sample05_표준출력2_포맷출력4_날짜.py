import  datetime
current_date = datetime.datetime.today()
print(current_date)
d = datetime.datetime(2021, 7, 13, 11, 39, 40)
print(d) #2021-07-13 11:39:40

'''
    SQL
    to_char(d, 'YYYY/MM/DD HH:MI:SS'
'''
#help("FORMATTING")
print("{:%Y년%m월%d   %H:%M:%S}".format(d))