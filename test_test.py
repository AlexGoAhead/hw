import random
b = []
for i in range(11):
    a = b.append(random.randint(-1, 1))
    # c = b.append(a)
print(b)
print('++++++++++++')

# print('----------')
# exmpl = [j for j in random(11) ]
# print(exmpl)

zxc = [i if i % 2 else "*" for a in range(11) for i in range(a) if a <=1]
print(i)
print(a)
sd = print([i if not i % 2 else '-' for a in range(5) for i in range(a) if a > 1])


ac = [random.randint(-1, 1) for i in range(11)]
print(ac)
print(len(ac))
print('8<-------------->8')
import operator
import random

def calc_frequency(lst):
    elem_sum = [lst.count(-1), lst.count(0), lst.count(1)]
    print(elem_sum)
    below_zero = elem_sum[0]
    zero = elem_sum[1]
    one = elem_sum[2]
    # b = list(a[2])
    # print(a)
    # print(b)
    if elem_sum[0] == elem_sum[1] or elem_sum[0] == elem_sum[2] or elem_sum[1] == elem_sum[2]:
        print(None)
        return None
    elif below_zero > zero and below_zero > one:
        print(-1)
        return -1
    elif zero > below_zero and zero > one:
        print(0)
        return 0
    elif one > below_zero or one > zero:
        print(1)
        return 1
    else:
        print('Error')
exm = calc_frequency([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1])
# res = calc_frequency([random.randint(-1, 1) for i in range(11)])