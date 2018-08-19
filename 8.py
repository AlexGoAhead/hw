# Дана строка с именем студента, в которой имя предшествует фамилии, например  ‘Mark Zuckerberg‘.
# Написать программу, которая преобразует эту строку, ставя фамилию на первое место, а имя на второе.
# Т.е. ‘Mark Zuckerberg‘ -> ‘Zuckerberg Mark‘.

name = 'Mark Zuckerberg'

first_name = name[:name.find(' ')]
surname = name[name.find(' ') + 1:]
print(surname + ' ' + first_name)
