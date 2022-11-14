# Вычислить число Пи c заданной точностью d
from math import pi

d =  int(input("Введите требуемую точност числа Пи: "))
print(f'Число Пи: {round(pi, d)}')
