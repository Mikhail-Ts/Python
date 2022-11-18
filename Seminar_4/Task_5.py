# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
import re

file1 = open('C:\\Users\\Михаил\\Desktop\\GB\\Python\\Python\\Seminar_4\\Polynominal_1.txt', 'r')
string1 = file1.read()
file2 = open('C:\\Users\\Михаил\\Desktop\\GB\\Python\\Python\\Seminar_4\\Polynominal_2.txt', 'r')
string2 = file2.read()
# print(f"Первый многочлен: {string1}")
# print(f"Второй многочлен: {string2}")

# Получаем коэффициенты из многочленов
numbers1 = (re.findall(r'(?<![x^]).(?<![= ])\d+', string1))
numbers2 = (re.findall(r'(?<![x^]).(?<![= ])\d+', string2))

# Выравниваем количество коэффициентов многочленов
if len(numbers1)!=len(numbers2):
    if len(numbers1) < len(numbers2):
        while len(numbers1) < len(numbers2):
            numbers1.insert(0,"0")
    else:
        while len(numbers1) > len(numbers2):
            numbers2.insert(0,"0")

# Находим сумму коэффициентов многочленов
sum_numbers = []
for i in range(len(numbers1)):
    sum_numbers.append(int(numbers1[i]) + int(numbers2[i]))
    i+=1

# Подготавливаем итоговый многочлен к выводу
s=len(sum_numbers)-1
def sum_polynom(s):
    polynom = ''
    for i in range(0, s+1):
        if s == 0:
            polynomial = (f'{sum_numbers[i]} = 0')
        elif s == 1:
            polynomial = (f'{sum_numbers[i]}x + ')
        else:
            polynomial = (f'{sum_numbers[i]}x^{s} + ')
        polynom += polynomial
        s -= 1
    return polynom

# print(sum_polynom(s))
# Вывод в файл
file =  open('C:\\Users\\Михаил\\Desktop\\GB\\Python\\Python\\Seminar_4\\Polynominal_sum.txt', 'w')
file.writelines(f'{sum_polynom(s)}\n')
file.close()

