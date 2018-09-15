student = ['Alex Goncharuk', 'Sergey Ivanov', 'Leonid Burlaka', 'Tom Jerry', 'Alexa Perry', 'Andrew Door', 'Jessica Timoty', 'Robert Queens', 'Terry Thomas', 'Berny Zayas']
frst_lst = []
scnd_lst = []
thrs_lst = []
frth_lst = []
for surname in student:
    b = surname.split()[1]
    if ord('%s' % b[0]) <= ord('G'):
        frst_lst.append(b)
    elif ord('J') >= ord('%s' % b[0]) <= ord('P'):
        scnd_lst.append(b)
    elif ord('Q') >= ord('%s' % b[0]) <= ord('T'):
        thrs_lst.append(b)
    elif ord('U') >= ord('%s' % b[0]):
        frth_lst.append(b)
print(frst_lst, scnd_lst, thrs_lst, frth_lst)

alst = []
blst = []
clst = []
dlst = []
for surname2 in student:
    b2 = surname2.split()[1]
    if ord('%s' % b2[0]) < ord('J'):
        alst.append(b2)
    elif ord('%s' % b2[0]) < ord('Q'):
        blst.append(b2)
    elif ord('%s' % b2[0]) < ord('U'):
        clst.append(b2)
    elif ord('%s' % b2[0]) <= ord('Z'):
        dlst.append(b2)
print(alst, blst, clst, dlst)
