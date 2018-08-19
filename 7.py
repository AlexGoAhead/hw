# Преобразовать строку с американским форматом даты в европейский. Например, '05.17.2016' преобразуется в '17.05.2016'
from datetime import datetime

dt = datetime.strptime('08.19.2018', '%m.%d.%Y')

print(str(dt.strftime('%d.%m.%Y')))


