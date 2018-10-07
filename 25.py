"""
Создайте список из всех нечётных чисел от 1 до 100 и передайте его в функцию,
которая переставляет его элементы в случайном порядке (например, 99 11 43 19 … 7 91 3 1).
	Примечание: использовать метод random.shuffle не допускается.

     def shuffle_list(list_to_shuffle): # no return (shuffles list in place)
		pass
"""
import random
def shuffle_list(list_to_shuffle):
    lst = len(list_to_shuffle)
    for i in range(len(list_to_shuffle)):
        a = random.randrange(0, 49)
        b = random.randrange(0, 49)
        list_to_shuffle[a], list_to_shuffle[b] = list_to_shuffle[b], list_to_shuffle[a]
        # print('Итерация цикла №:', i)
        # print('Индекс а: %d и соответственно индекс b: %d' % (a, b))
    print('Список после перешивания:', 'Элементов в списке:%d ' % len(list_to_shuffle), list_to_shuffle, sep='\n')
    print('Список отсортированный после перемешивания, для проверки неизменности списка и количества элементов в нем: ', 'Элементов в списке:%d ' % len(list_to_shuffle), sorted(list_to_shuffle), sep='\n')
        # print('-----------------')
res = shuffle_list([i for i in range(1, 100) if i % 2 != 0])



