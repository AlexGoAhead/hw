""""
Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа,
введенного пользователем в консоли,
без использования операторов цикла. a) cо строками, б) без использования строк.
def sum_of_digits(number): # returns int
			pass
"""

def sum_of_digits(number):
    number = str(number)
    digit = (int(number[:1]) + int(number[1:2]) + int(number[2]))
    return digit
print(sum_of_digits(123))

def sum_of_digits(number):
    return number
result = sum_of_digits(123)
print((result % 10) + ((result//10) % 10) + (result // 100))