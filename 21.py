'''''Написать функцию возвращающую наибольшую цифру 
случайно сгенерированного 12 ти-значного натурального числа. 
a) c использованием строк, b) без использования строк.
def get_max_digit(number): # returns int
		     pass
'''''
import random

def get_max_digit(number):
    # number = random.sample(range(000000000000, 1000000000000), 12)
    maxval = number
    max_val_string = str(maxval)
    return int(max(str(max_val_string)))
res = get_max_digit(568504332454)
print(res)