from time import ctime
from datetime import datetime
import datetime
from datetime import datetime,date



# // Day {Mon,Tue,..}
# print(ctime())
#
# print(ctime().split()[2]+'.'+ctime().split()[1]+'.'+ctime().split()[4])

# today1 = datetime.date()
# print(today1)

text = 'butter, egg, hunger'
print(text.split(':'))
print(text.split(',', 4))
dt = '05.17.2016'
print(dt.split('.', 3))
print(dt.split()[1])
# import datetime
# date_time = str(datetime.datetime.now())
# date = date_time.split()[0]
# time = date_time.split()[1]
# print(date, time)
# print(datetime.datetime.now().split())

import datetime
from time import ctime


# date_time = str(datetime.datetime.now())
# date = date_time.split()[0]
# time = date_time.split()[1]
# print (date)

# str = ("08.19.2018", '%m, %d, %Y')
# print(str.split('%m, %d, %Y'))
# print(str.split('%d, %m, %Y'))
