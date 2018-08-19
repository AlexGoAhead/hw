# Найти результат выражения для произвольных значений a,b,c: (a - b * c ) / ( a + b ) % c

a = 5
b = 10
c = 15
summary = (a - b * c) / (a + b) % c
print('The result of equation is', summary)

# хочу спросить, почему когда я делаю ответ через ссылку на результат с помощью "%2.f",
# то результат не получается с двумя знаками после запятой?
print('The result of equation is %2.f' % summary)
