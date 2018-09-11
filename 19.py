"""
Написать функцию для поиска разницы между максимальным
и минимальным числом среди num_limit случайно сгенерированных чисел
в указанном числовом диапазоне.
		def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
			pass
"""
import random
def diff_min_max(num_limit, lower_bound, upper_bound):
    num_limit = [i for i in range(random.randint(lower_bound, upper_bound))]
    return int(max(num_limit)) - int(min(num_limit))
result = diff_min_max([30], 1, 10)
print(result)