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
    final_list = []
    a = lst.count(1)
    b = lst.count(-1)
    c = lst.count(0)
    ab = final_list.append(lst.count(1))
    bc = final_list.append(lst.count(-1))
    cd= final_list.append(lst.count(0))
    if final_list[0] == final_list[1]:
        print(None)
        return None
    elif final_list[1] == final_list[2]:
        print(None)
        return None
    elif final_list[0] == final_list[2]:
        print(None)
        return None
    else:
        if a > b and c:
            print('number of 1 is: ', a)
            return 1
        elif b > a and c:
            print('number of -1 is: ', b)
            return -1
        elif c > a and b:
            print('number of 0 is: ', c)
            return 0
        else:
            print(lst)
    print(lst)
    # print(a, b, c)
    print(final_list)
    print(lst)
# ex = calc_frequency([1, 1, 1, -1, -1, 1, 1, -1, 0, 0, 0])
exmpl = calc_frequency([random.randint(-1, 1) for i in range(11)])

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