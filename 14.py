"""
Написать функцию, которая будет проверять четность некоторого числа.
		def is_even(number): # returns boolean value
			pass
"""

def is_even(number):
    return number % 2 == 0
print('Некоторое число является четным, и это утверждение: %s' % is_even(12345678))