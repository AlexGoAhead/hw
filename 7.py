# Преобразовать строку с американским форматом даты в европейский. Например, '05.17.2016' преобразуется в '17.05.2016'
from datetime import datetime

# dt = datetime.strptime('08.22.2018', '%m.%d.%Y')
# print(str(dt.strftime('%d.%m.%Y')))



import datetime

d = datetime.datetime.now()
b = str(d)
date = b.split()[0]
date_lst = date.split('-')
li = [date_lst]
# print(d)
# print(m)
print('USA date format is:', date_lst[1] + '.' + date_lst[2] + '.' + date_lst[0])
print('EU date format is:', date_lst[2] + '.' + date_lst[1] + '.' + date_lst[0])

