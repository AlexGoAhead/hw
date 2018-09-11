from random import randint
import random
from random import sample

# def nums (num_limit, lower, upper):
#     num_limit = 20
#     # num_limit = [randint(lower, upper) for i in range(len(num_limit))]
#     num_limit = sample(range(lower, upper), 20)
#     # nums1 = [i for i in range(len(num_limit)) if i % 2 == 0]
#     # nums2 = [i for i in range(len(num_limit)) if i % 2 != 0]
#     even_nums = [i for i in num_limit if i % 2 == 0]
#     odd_nums = [i for i in num_limit if i % 2 != 0]
#     # num_random = random.Random(nums3)
#     # return sum(even_nums) - sum(odd_nums)
#     return sum(even_nums) - sum(odd_nums)
# ress = nums([20], 1, 30)
# print(ress)
# print('Разница между четныйми и не четными списками по сумме будет равна: ', int(sum(ress[:1])))


# list2 = sample(range(1, 20), 5)
# list = sample(range(-10, 11), 20)
# s = int(list2)
# print(list)
# print(list2)

a = 1004
b = str(a)
print(b[0])

def get_max_digit(number):
    # number = random.sample(range(000000000000, 1000000000000), 12)
    maxval = number
    max_val_string = str(maxval)
    return int(max(str(max_val_string)))
res = get_max_digit(568504332454)
print(res)