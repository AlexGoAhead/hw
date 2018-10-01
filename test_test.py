import random
lst = [i for i in range(10) if i % 2 != 0]
print(lst)
new_lst = 0
x = []
while new_lst < len(lst):
    # print(lst[new_lst])
    m = lst[random.choice], lst[random.choice] = lst[random.choice], lst[random.choice]
    num = x.append(lst[new_lst])
    new_lst += 1
print(x)
print(m)