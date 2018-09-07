'''
Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
Каждая окружность задается координатами центра и радиусом.
def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
			pass
	Примечание: варианты взаимного пересечения окружностей: http://bit.ly/2D7ILFg
'''
import math


def circles_intersect(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
    if distance == r1 - r2:
        print('Две заданные окружности пересекаются касательно с внутренней стороны')
        return True
    elif distance == r1 + r2:
        print('Две заданные окружности пересекаются касательно с внешней стороны')
        return True
    elif abs(r1 - r2) < distance < r1 + r2:
        print('Две заданные окружности пересекаются имеют две точки пересечения')
        return True
    else:
        return False
result = circles_intersect(0, 0, 5, 0, 0, 5)
print(result)
