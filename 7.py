# Преобразовать строку с американским форматом даты в европейский. Например, '05.17.2016' преобразуется в '17.05.2016'
from datetime import datetime

# dt = datetime.strptime('08.22.2018', '%m.%d.%Y')
# print(str(dt.strftime('%d.%m.%Y')))



import datetime

d = datetime.datetime.now()
b = str(d)
m = b.split()[0]
n = m.split('-')
li = [n]
# print(d)
# print(m)
print('USA date format is:', n[1] + '.' + n[2] + '.' + n[0])
print('EU date format is:', n[2] + '.' + n[1] + '.' + n[0])

