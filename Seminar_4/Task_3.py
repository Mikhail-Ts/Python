# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def UniqList (list):
    list = [i for i in list if list.count(i) == 1]
    return list

list = list(input("Введите числа через пробел: "))
print (UniqList(list))