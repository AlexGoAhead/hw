import random

def diff_min_max(num_limit, lower_bound, upper_bound):
   num_limit = [i for i in range(random.randint(lower_bound, upper_bound))]
   for j in range(len(num_limit)):
       num_limit[j] = random.shuffle(num_limit)
   return num_limit[j]
result = diff_min_max([30], 1, 10)
print(result)