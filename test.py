students = ['Alex Goncharuk', 'Sergei Petrov', 'Leonib Burlaka', 'Victoria Goncharuk']
srnm = [i for i in students]
print(range(len(srnm)))
a = students[0]
b = a.rfind(' ')
print('------')
print(b)
print('------')

text = 'Ваши действия в режиме инкогнито будут недоступны другим пользователям этого устройства. Однако закладки и скачанные файлы сохранятся'
word_lengths = [len(word.strip('.,!@#$%^&*?')) for word in text.split()]
print(word_lengths)
print('Avr. length:', sum(word_lengths) // len(word_lengths))

print("Поможет выполнить задание!!!!")
group_firts = [chr(i) for i in range(ord('A'), ord('I') + 1)]
print(group_firts)
print(''.join(group_firts))

second_group = [chr(i) for i in range(ord('J'), ord('P') + 1)]
print(second_group)
print(''.join(second_group))

third_group = [chr(i) for i in range(ord('Q'), ord('T') + 1)]
print(third_group)
print(''.join(third_group))

fourth_group = [chr(i) for i in range(ord('U'), ord('Z') + 1)]
print(fourth_group)
print(''.join(fourth_group))