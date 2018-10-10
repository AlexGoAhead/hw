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
import collections
from collections import Counter
def calc_frequency(lst):
    below_zero = []
    zero = []
    one = []
    a = lst.count(1)
    b = lst.count(-1)
    c = lst.count(0)
    if a > b and c:
        print('number of 1 is: ', a)
        return a
    elif b > a and c:
        print('number of -1 is: ', b)
        return b
    elif c > a and b:
        print('number of 0 is: ', c)
        return c
    elif b == c:
        print(None)
        return None
    else:
        print(None)
        return None
        if a == b or a == c or b == c or b == a or c == a:
            print(None)
            return None
    print(lst)
    print(a, b, c)
ex = calc_frequency([1, 1, 1, -1, -1, 1, 1, -1, 0, 0, 0])
# exmpl = calc_frequency([random.randint(-1, 1) for i in range(11)])

#
# Сколько
# раз
# входит
# число
# 7
# в
# список
# a


def mycount(a):
    c = 0
    for x in a:
        if x == 7:
            c = c + 1
    return c


a = [7, 9, -3, 7, 2, 1, 7]
# print(mycount(a))