# Задача 10:
# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

c_amt = int(input('Введите количество монет: '))
count_reshka = 0
count_gerb = 0
for i in range(c_amt):
    side = int(input('Введите какой стороной упала каждая монетка (решка = 1, герб = 0): '))
    if side == 1:
        count_reshka += 1
    else:
        count_gerb += 1
if count_reshka <= count_gerb:
    print(f'Нужно перевернуть {count_reshka} монет')
else:
    print(f'Нужно перевернуть {count_gerb} монет')
