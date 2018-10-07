import random
# lst = []
# for _ in range(100):
#     x = lst.append(random.randrange(1, 100, 2))
# # print(x)
# print(lst)


# print(random.randrange(1, 100, 2))
# exmpl = lst[random.randrange(1, 100, 2)]
#
# exmpl_second = lst[random.randrange(1, 100, 2)]
# print(exmpl, exmpl_second)
# print(lst[random.randrange(1, 100, 2)])
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = random.randrange(0, 9)
# b = random.randrange(0, 9)
# lst[a], lst[b] = lst[b], lst[a]
    for i in range(len(lst)):
        a = random.randrange(0, 10)
        b = random.randrange(0, 10)
        lst[a], lst[b] = lst[b], lst[a]
print(lst)





