import random

result = []
b = []
c = []
chislo = range(3, 20)
a = random.choice(chislo)
print(f'Введите пароль для числа: {a}')

for i in range(1, a):
    for j in range(1, i):
        if a == i + j or a % (i + j) == 0:
            b.extend([j])
            c.extend([i])
            print(f'Пароль: {j} {i}')
        else:
            continue
result = sorted(list(zip(b, c)))
print(f'Подходящие пароли: {result}')