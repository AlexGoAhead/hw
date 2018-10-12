"""
Создайте список из 11 случайных целых чисел из отрезка [-1;1].
Передайте его в функцию, которая определит какой элемент встречается в списке чаще всего и вернет этот элемент.
Однако, если два каких-то элемента встречаются одинаковое количество раз, то вернуть None,
а не самый часто встречающийся элемент, даже если дублирующиеся элементы не максимальны!
     def calc_frequency(lst): # returns the most frequent number or None
		pass
	Например:
		для [1, 1, 1, -1, -1, 1, 1, -1, 0, 0, 0] надо вернуть None
		для [1, 1, 1, 1, -1, 1, 1, -1, 0, 0, 0] надо вернуть 1

"""

import random

def calc_frequency(lst):
    elem_sum = [lst.count(-1), lst.count(0), lst.count(1)]
    print(elem_sum)
    below_zero = elem_sum[0]
    zero = elem_sum[1]
    one = elem_sum[2]
    # b = list(a[2])
    # print(a)
    # print(b)
    if elem_sum[0] == elem_sum[1] or elem_sum[0] == elem_sum[2] or elem_sum[1] == elem_sum[2]:
        print(None)
        return None
    elif below_zero > zero and below_zero > one:
        print(-1)
        return -1
    elif zero > below_zero and zero > one:
        print(0)
        return 0
    elif one > below_zero or one > zero:
        print(1)
        return 1
    else:
        print('Error')
res = calc_frequency([random.randint(-1, 1) for i in range(11)])