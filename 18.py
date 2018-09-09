'''''
Каждому символу в таблице символов Unicode соответствует число. 
Написать функцию, которая рассчитывает сумму чисел, которые соответствуют символам, стоящим между двумя заданными включительно. 
Например, в функцию передаются символы ‘x’ и ‘z’. Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’. 
		def sum_symbol_codes(first, last): # returns int
			pass
'''''
import string


def sum_symbol_codes(first, last):
    alphabet = string.ascii_letters
    a = alphabet.find(first)
    z = alphabet.find(last)
    result = alphabet[a:z + 1]
    count = 0
    for i in result:
        # print(ord(i))
        count = count + ord(i)
    return count
res = sum_symbol_codes('a', 'k')
print(res)




# def calc_sum_of_n(n):
#     total_sum = 0
#     for i in range(1, n+1):
#         total_sum = total_sum + i
#     return total_sum
#
# print('Total sum:', calc_sum_of_n(100))


'''''''''''
test = input(str())
print(ord(test))

def alf_to_unicode(alf):
    alf = str(ord())
    return alf
print(str(alf_to_unicode('j')))
'''''



# s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for c in string.ascii_uppercase:
#     print(c, '=', ord(c))
# for v in string.ascii_lowercase:
#     print(v, '=', ord(v))

# h = "a\xac\u1234\u20ac\U00008000"
# print([ord(c) for c in h])

# u = 'abcdé'
# print(ord(u[-1]))



# import re
# q = string.ascii_letters
# print(q[3:7])
# # print(q[int(input()):7])
# test_test = q.find(input())
# test_test2 = q.find(str(input()))
# # print(test_test)
# # test2 = q[test_test:9]
# test3 = q[test_test:test_test2+1]
# # print(test3)
# for g in test3:
#     print(ord(g))
#     box = 0
#     for integ in ord(g):
#         try:
#             value = int(integ)
#             box += value
#         except:
#             pass
#     print(box)

# print('8<------------->8')
# print(ord('a'))
# print(ord('b'))
# print(ord('c'))