# Найти результат выражения для произвольных значений a,b,c: | a - b | /( a + b)3 - cos( c )
import math

a = 5
b = 10
c = 15
# |a - b| = (a + b)
summary = (a + b) / (a + b)**3 - math.cos(c)
print('The result of equation is', summary)
