'''
Для удобства проведения вступительных экзаменов всеx абитуриентов в MIT разбивают на группы
в зависимости от первых букв их фамилии. Группы называются ‘A-I’, ‘J-P’, ‘Q-T’, ‘U-Z’.
Название группы определяет в какую группу попадает абитуриент, в зависимости от первой буквы его/ее фамилии.
Например, Will Smith попадает в группу ‘Q-T’, т.к. первая буква его фамилии попадает в диапазон букв от ‘Q‘ до ‘Т‘ (включительно!).
Абитуриент Jay Z попадает в группу ‘U-Z’ и т.д.
Написать функцию, которая получает список имен студентов вида ['Name1 Surname1', 'Name2 Surname2', 'Name3 Surname3', ...]
и возвращает количество абитуриентов в группах, сформированных по их фамилиям, описанным выше образом.
     def group_by_surname(list_of_enrollees): # returns 4 ints

'''

def group_by_surname(list_of_enrollees):
    a2i = []
    j2p = []
    q2t = []
    u2z = []
    for surname2 in list_of_enrollees:
        surname = surname2.split()[1]
        if ord('%s' % surname[0]) < ord('J'):
            a2i.append(surname)
        elif ord('%s' % surname[0]) < ord('Q'):
            j2p.append(surname)
        elif ord('%s' % surname[0]) < ord('U'):
            q2t.append(surname)
        elif ord('%s' % surname[0]) <= ord('Z'):
            u2z.append(surname)
    return len(a2i), len(j2p), len(q2t), len(u2z)
print(group_by_surname(['A I', 'B J', 'C T', 'D U']))