from random import randint

x = randint(100, 200)
y = randint(0, 100)

print(f'Целочисленное деление чисел {x}, {y} = {x//y}')
print(f'Остаток от деления чисел {x}, {y} = {x%y}')