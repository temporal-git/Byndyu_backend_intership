from random import randint

num = []
for j in range(1000):
    value = randint(1, 100)
    num.append(value)

for i in num:
    open('../performance/gen_arr.txt', 'w').write(str(i) + '\n ')

