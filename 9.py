# Написать программу, которая преобразует имя переменной в формате snake_case в формат CamelCase.
# Для простоты считаем, что имя переменной всегда состоит из 3-х слов.
# Например: 'employee_first_name' -> 'EmployeeFirstName'

import re

text = 'snake_case'
result = re.sub(r'_', '', text)


print(result)
