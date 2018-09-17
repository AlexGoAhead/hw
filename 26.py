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
# def calc_frequency(lst):
    # lst_first = []
    # for i in
    # print(a)
lst = []
lst1 = []
for i in range(11):
    lst.append(random.randint(-1, 1))
for j in range(11):
    lst1.append(random.randint(-1, 1))
print(lst)
print(list(collections.Counter(lst))[2])
print('-----')
print(lst1)
test = collections.Counter(lst1)
print(collections.Counter(lst1))
print('------')
print(test['1'])
print(list(lst1.keys())[list(lst1.values()).index(1)])