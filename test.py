import random
lst = [i for i in range(10) if i % 2 != 0]
print(lst)
new_lst = 0
x = []
while len(lst) != 0:
    # print(lst[new_lst])
    new_lst += 1
    metr = random.choice(list(lst))
    num = x.append(metr)
    lst.remove(metr)
print(x)