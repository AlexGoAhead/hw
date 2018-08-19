# Найти результат выражения для произвольных значений a,b,c: ( ln( 1 + c ) / -b )4+ | a |
import math

a = 5
b = 10
c = 15
# math.log(1+c)
summary = (math.log(1 + c) / -b)**4 + math.fabs(a)
print('The result of equation is', summary)

# тот же самый момент
print('The result of equation is %2.f' % summary)
