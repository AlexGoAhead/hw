'''''
Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел среди num_limit 
случайно сгенерированных чисел в указанном числовом диапазоне. 
Т.е. от суммы четных чисел вычесть сумму нечетных чисел.
		def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int
		     pass
'''''
import random
def diff_even_odd(num_limit, lower_bound, upper_bound):
    num_limit = random.sample(range(lower_bound, upper_bound), 20)
    even_nums = [i for i in num_limit if i % 2 == 0]
    odd_nums = [i for i in num_limit if i % 2 != 0]
    return num_limit, even_nums, odd_nums, print('Difference between nums is: ', (sum(even_nums) - sum(odd_nums)))
result = diff_even_odd([20], 1, 30)
print(result)
print('The End')