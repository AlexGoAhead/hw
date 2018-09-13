a = 64
b = (2**20)-1
# print(b)
def play_game():
    summary_chess = 2**64 - 1
    for i in range(1, 65):
        q = 2**i-1
        m = 2**i-1
        print('Сумма зерен на %d ячейке будет равна: %d' % (i, q))
        if q >= 1000000 and q < 2000000:
            # print(list(enumerate(range(q))))
            print(q)
    return q, m
play_game()

print(2**64-1)
print('*****************')

print('*****************')
def chess_reward():
   for i in range(1, 65):
       total_number = 2**i -1
       if total_number >= 1000000 and total_number < 2000000:
           l = total_number
           print(l)
   return print(total_number)
chess_reward()