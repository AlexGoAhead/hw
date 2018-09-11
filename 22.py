"""
Случайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать.
Пользователь вводит число, а программа проверяет его и, если пользователь не угадал, то говорит больше или меньше.
После чего опять просит угадать. И так пока пользователь не угадает выбранное число.
"""
from random import randint
def loto_digit(number):
    true_num = randint(1, 10)
    print('Please, try to guess the number in the range of 1 - 10: ')
    while True:
        a = int(input())
        if a == 0: break
        if a != true_num:
            if a > true_num:
                print('Try reduce your number')
            elif a < true_num:
                print('Try to increase your number')
        else:
            print('Bingo')
            print(true_num)
result = loto_digit(input('Press enter to start'))