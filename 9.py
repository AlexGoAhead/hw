# Написать программу, которая преобразует имя переменной в формате snake_case в формат CamelCase.
# Для простоты считаем, что имя переменной всегда состоит из 3-х слов.
# Например: 'employee_first_name' -> 'EmployeeFirstName'

snk_cs = 'one_two_three'
include = snk_cs.split('_')
# print(include)
first_word = include[0]
second_word = include[1]
third_word = include[2]
print('CamelCase format is:', first_word.title() + second_word.title() + third_word.title())
