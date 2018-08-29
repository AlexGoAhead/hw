# Написать функцию, которая будет переводить градусы в радианы (без использования math.radians).
# Используя эту функцию, вывести на экран значения косинусов углов в 60, 45 и 40 градусов.
# def degrees2radians(degrees): # returns float
# 			pass

import math

def degrees2radians(degrees):
    return (degrees*math.pi)/180
dgrs1 = degrees2radians(math.cos(60))
dgrs2 = degrees2radians(math.cos(45))
dgrs3 = degrees2radians(math.cos(40))
print('%.2f %.2f %.2f' % (dgrs1, dgrs2, dgrs3))
