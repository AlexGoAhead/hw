# Дана строка вида 'Leo Tolstoy*1828-08-28*1910-11-20'.
# В этой строке указаны имя писателя и через символ * даты рождения и смерти.
# Даты указаны в формате "YYYY-MM-DD".
# Требуется написать программу, которая по переданной строке определит возраст писателя и распечает его имя и возраст.
# Например, для строки 'Leo Tolstoy*1828-08-28*1910-11-20' программа должна распечает: 'Leo Tolstoy, 82'.
# Для строки 'Marcus Aurelius*121-04-26*180-03-17' - 'Marcus Aurelius, 59'.
# Примечание: Т.к. имена писателей могут быть разной длины, то индексы символов разделителей ('*', '-') будут разными!
# Месяцы и дни для определения возраста можно игнорировать.
from datetime import datetime
import re
date_of_life = 'Leo Tolstoy*1828-08-28*1910-11-20'
list = date_of_life.split('*')
name_surname = list[0]
date1 = list[1]
date2 = list[2]
year1 = date1.split('-')[0]
year2 = date2.split('-')[0]
total_age = int(year2) - int(year1)
print(name_surname + ',', total_age)

date_of_life = 'Marcus Aurelius*121-04-26*180-03-17'
list = date_of_life.split('*')
name_surname = list[0]
date1 = list[1]
date2 = list[2]
year1 = date1.split('-')[0]
year2 = date2.split('-')[0]
total_age = int(year2) - int(year1)
print(name_surname + ',', total_age)
