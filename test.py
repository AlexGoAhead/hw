
# name = input('Enter you name: ')
# year = input('How old are you: ')
# hundred_year = (2018 - int(year))+100
# print('%s, you 100 year in %d year!' % (name, hundred_year))
from random import randint
print('Please, try to guess the number in the range of 1 - 10: ')

number = randint(1, 10)
while True:
    a = int(input())
    if a == 0: break
    if a != number:
        if a >number:
            print('Try reduce your number')
        elif a < number:
            print('Try to increase your number')
    else:
        print('Bingo')
        print(number)