'''''
Два поезда движутся на скорости V1 и V2 навстречу друг другу. 
Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь. 
При заданных скоростях узнать столкнутся ли поезда.
def have_trains_crashed(v1, v2): # returns boolean value
			pass
'''''
# S = distance
# V = speed
# t = time
# X = условная переменная "Скорость сближения" (V1 + V2)
def have_trains_crashed(v1, v2):
    dist_summ = 10
    dist1 = 4
    dist2 = dist_summ - dist1
    time1 = dist1 / v1
    time2 = dist2 / v2
    if time1 >= time2:
        print('При заданной скорости поезда не столкнутся!')
        return True
    else:
        print('При заданной скорости поезда'
              ' столкнутся!')
        return False
result = have_trains_crashed(2, 1)
print(result)
