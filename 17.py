'''''
Написать функцию решения квадратного уравнения.  
		def solve_quadratic_equation(a, b, c): 
		# always returns 2(!) 
		values: either 2 roots, 1 root and None or 2 Nones
			pass
'''''
import math


def solve_quadratic_equation(a, b, c):
    discriminant = (b**2) - (4 * a * c)
    if discriminant > 0:
        root1 = ((-b + math.sqrt(discriminant)) / (2 * a))
        root2 = ((-b - math.sqrt(discriminant)) / (2 * a))
        print('Дискриминант имеет два корня: %d and %d ' % (root1, root2))
        return root1, root2
    elif discriminant == 0:
        root1 = (-b / (2 * a))
        root2 = None
        print('Дискриминант имеет один корень: %d and %s ' % (root1, root2))
        return root1, root2
    elif discriminant < 0:
        root1 = None
        root2 = None
        print('Дискриминант имеет один корень:%s and %s ' % (root1, root2))
        return root1, root2

result = solve_quadratic_equation(1, -40, 400)
print('The End')


# m = 'Hello World!'
# for n in m:
#     print(n)
#
# z = 'Alex+Go+Ahead'
# x = z.split('+')
# for v in x:
#     print(v)

