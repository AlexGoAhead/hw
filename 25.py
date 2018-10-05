"""
Создайте список из всех нечётных чисел от 1 до 100 и передайте его в функцию,
которая переставляет его элементы в случайном порядке (например, 99 11 43 19 … 7 91 3 1).
	Примечание: использовать метод random.shuffle не допускается.

     def shuffle_list(list_to_shuffle): # no return (shuffles list in place)
		pass
"""
from random import randrange
def shuffle_list(list_to_shuffle):
    # m = [list_to_shuffle[i^1] for i in range(len(list_to_shuffle))]
    # print(list_to_shuffle)
    for i in range(len(list_to_shuffle)):
        a = randrange(list_to_shuffle.__len__())
        b = randrange(list_to_shuffle.__len__())
        list_to_shuffle[a], list_to_shuffle[b] = list_to_shuffle[b], list_to_shuffle[a]
    print(list_to_shuffle)
    print(sorted(list_to_shuffle))
res = shuffle_list([i for i in range(100) if i % 2 != 0])



