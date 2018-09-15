"""
Создайте список из всех нечётных чисел от 1 до 100 и передайте его в функцию,
которая переставляет его элементы в случайном порядке (например, 99 11 43 19 … 7 91 3 1).
	Примечание: использовать метод random.shuffle не допускается.

     def shuffle_list(list_to_shuffle): # no return (shuffles list in place)
		pass
"""
import random
def shuffle_list(list_to_shuffle):
    oracle = list_to_shuffle
    shuffled_list = random.sample(oracle, len(oracle))
    print(shuffled_list)
    # print(sorted(shuffled_list))
res = shuffle_list([i for i in range(100) if i % 2 != 0])
