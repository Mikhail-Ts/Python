# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Программа до улучшения
# def UniqList (list):
#     list = [i for i in list if list.count(i) == 1]
#     return list

# list = list(input("Введите числа через пробел: "))
# print (UniqList(list))


# Программа после
list1 = list(input("Введите числа через пробел: "))
list2 = list(filter(lambda i: list1.count(i) == 1,list1))
print (list2)
