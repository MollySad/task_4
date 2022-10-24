from random import randint

int_1 = randint(0, 100)
int_2 = randint(0, 100)
int_3 = randint(0, 100)

print(f'Среднее значение чисел {int_1}, {int_2}, {int_3} = {(int_1 + int_2 + int_3) / 3:.0f}')