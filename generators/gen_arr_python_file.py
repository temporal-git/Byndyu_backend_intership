from random import randint

num = []
for j in range(1000):
    value = randint(1, 100)
    num.append(value)

open('../data/py_arr.py', 'w').write('digi_list = [')

for i in num:
    open('../data/py_arr.py', 'a').write(str(i) + ', ')

open('../data/py_arr.py', 'a').write(']')



