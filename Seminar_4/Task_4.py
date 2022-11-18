# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random as r

def polynom(s):
    polynom = ''
    for i in range(0, s+1):
        k = r.randint(1, 100)
        if s == 0:
            polynomial = (f'{k} = 0')
        elif s == 1:
            polynomial = (f'{k}x + ')
        else:
            polynomial = (f'{k}x^{s} + ')
        polynom += polynomial
        s -= 1
    return polynom

s = int(input('Введите натуральное число степени:'))

# result = polynom(s)
# print(result)

file =  open('C:\\Users\\Михаил\\Desktop\\GB\\Python\\Python\\Seminar_4\\Polynominal_Task_4.txt', 'w')
file.writelines(f'{polynom(s)}\n')
file.close()