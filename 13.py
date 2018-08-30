'''
Написать функцию, которая вычислит площадь и объем конуса по его радиусу и высоте.
Результат работы функции должен вернуть два значения.
def cone_square_and_volume(radius, height): # returns 2 floats
			pass
'''
import math


def cone_square_and_volume(radius, height):
	result = (math.pi * radius) * (radius + (math.sqrt(radius**2 + height**2)))
	result1 = 1/3 * math.pi * radius**2 * height
	return result, result1
result2 = cone_square_and_volume(3, 2)
print('Result: ', result2)
